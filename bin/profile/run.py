#!/usr/bin/env python3
"""Runs primitives.md / instructions.md against configured models and, by
default, synthesizes a cross-model metastudy from the results.

Each `##` section in instructions.md becomes one conversation turn -- all of
that section's numbered questions are sent together in a single message, and
the reply is written to its own file. Each model gets its own self-contained
folder (YYYYMMDD/<provider>__<label>/), with its own manifest.json alongside
its section files -- no shared file that every model run has to coordinate
writes to.

No selection flags + a real terminal -> interactive menu (pick a model,
run it, repeat; 'a' for all, 'm' for metastudy-only, 'x' to quit).

Usage:
    python run.py                       # interactive menu
    python run.py --all                 # every configured model, no menu
    python run.py --date 20260719
    python run.py --only anthropic      # skip Ollama
    python run.py --models haiku-4-5    # just one, by its models.yaml label
    python run.py --skip-metastudy      # collect transcripts only
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from rich.prompt import Prompt
from rich.table import Table
import yaml

from lib.metastudy import build_metastudy
from lib.ollama_service import OllamaService
from lib.pricing import estimate_cost, format_usd
from lib.providers import get_provider

PROFILE_DIR = Path(__file__).parent
PRIMITIVES_PATH = PROFILE_DIR / "primitives.md"
INSTRUCTIONS_PATH = PROFILE_DIR / "instructions.md"
REFERENCE_PATH = PROFILE_DIR.parent.parent / "reference.md"
MODELS_CONFIG_PATH = PROFILE_DIR / "models.yaml"

SECTION_RE = re.compile(r"^##\s+(.*)")
ITEM_RE = re.compile(r"^\d+\.\s+(.*)")
SLUG_RE = re.compile(r"[^a-z0-9]+")

console = Console()
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console, rich_tracebacks=True, show_path=False, markup=True)],
)
# The Anthropic SDK's own httpx/httpcore request logging inherits the root
# handler above -- keep it to warnings-and-worse so it doesn't drown out our
# own INFO lines with a "HTTP Request: POST ... 200 OK" per API call.
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
log = logging.getLogger("uriam")


def slugify(text: str) -> str:
    return SLUG_RE.sub("-", text.lower()).strip("-")


def parse_sections(path: Path) -> list[tuple[str, list[str]]]:
    """Returns ordered (section, questions) pairs -- one entry per `##`
    section in instructions.md, with that section's numbered questions in
    their original order."""
    sections: list[tuple[str, list[str]]] = []
    current_section: str | None = None
    current_questions: list[str] = []
    for line in path.read_text().splitlines():
        header_match = SECTION_RE.match(line)
        if header_match:
            if current_section is not None:
                sections.append((current_section, current_questions))
            current_section = header_match.group(1).strip()
            current_questions = []
            continue
        item_match = ITEM_RE.match(line)
        if item_match and current_section is not None:
            current_questions.append(item_match.group(1).strip())
    if current_section is not None:
        sections.append((current_section, current_questions))
    return sections


def git_sha_for(path: Path) -> str | None:
    result = subprocess.run(
        ["git", "log", "-1", "--format=%H", "--", str(path)],
        cwd=path.parent,
        capture_output=True,
        text=True,
    )
    sha = result.stdout.strip()
    return sha or None


def model_dir_for(run_dir: Path, provider: str, label: str) -> Path:
    return run_dir / f"{provider}__{label}"


def save_model_manifest(model_dir: Path, manifest: dict) -> None:
    manifest["updated_at"] = datetime.now(timezone.utc).isoformat()
    (model_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))


def run_model(
    label: str,
    provider: str,
    model: str,
    system: str,
    sections: list[tuple[str, list[str]]],
    model_dir: Path,
) -> tuple[list[str], int, int]:
    """Runs one turn per section (that section's questions batched together),
    writing each section's transcript to its own file as soon as it
    completes -- so a later section failing doesn't lose earlier progress.

    Returns (written file names, total_input_tokens, total_output_tokens).
    """
    client = get_provider(provider, model)
    messages: list[dict] = []
    total_input_tokens = 0
    total_output_tokens = 0
    written: list[str] = []

    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.fields[label]}[/]"),
        BarColumn(),
        TextColumn("{task.completed}/{task.total}"),
        TextColumn("[dim]{task.fields[current]}[/]"),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("run", total=len(sections), label=label, current="")
        for index, (section, questions) in enumerate(sections, start=1):
            progress.update(task, current=f"[{index}/{len(sections)}] {section}")

            prompt = "\n".join(f"{i}. {q}" for i, q in enumerate(questions, start=1))
            messages.append({"role": "user", "content": prompt})
            reply = client.send(messages, system=system)
            messages.append({"role": "assistant", "content": reply.text})

            total_input_tokens += reply.input_tokens
            total_output_tokens += reply.output_tokens
            if reply.truncated:
                log.warning(f"{label} section {index}/{len(sections)} [{section}] hit max_tokens -- reply may be cut off")

            file_content = "\n".join([
                f"# {label} ({provider} / {model}) — {section}",
                "",
                f"Run: {datetime.now(timezone.utc).isoformat()}",
                f"Section {index}/{len(sections)}",
                "",
                "System prompt: primitives.md, verbatim (see ../../primitives.md).",
                "",
                "## Questions",
                "",
                prompt,
                "",
                "## Response",
                "",
                reply.text,
                "",
            ])
            filename = f"{index:02d}-{slugify(section)}.md"
            (model_dir / filename).write_text(file_content)
            written.append(filename)
            progress.advance(task)

    return written, total_input_tokens, total_output_tokens


def run_one(
    spec: dict,
    run_dir: Path,
    system_prompt: str,
    sections: list[tuple[str, list[str]]],
    shas: tuple[str | None, str | None],
    ollama_service: OllamaService,
) -> None:
    label, provider, model = spec["label"], spec["provider"], spec["model"]
    primitives_sha, instructions_sha = shas
    model_dir = model_dir_for(run_dir, provider, label)

    # Wipe any previous run of this model today so a rerun never leaves
    # stale/mismatched files (e.g. from an older instructions.md shape)
    # sitting alongside fresh ones.
    for stale in model_dir.glob("*"):
        stale.unlink()
    model_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "date": run_dir.name,
        "provider": provider,
        "model": model,
        "label": label,
        "primitives_sha": primitives_sha,
        "instructions_sha": instructions_sha,
    }

    log.info(f"[bold]{label}[/] ({provider}/{model}) starting")
    try:
        if provider == "ollama":
            ollama_service.ensure_running()

        written, input_tokens, output_tokens = run_model(label, provider, model, system_prompt, sections, model_dir)
        cost = estimate_cost(input_tokens, output_tokens, spec.get("price_in"), spec.get("price_out"))
        cost_line = format_usd(cost, free=(provider == "ollama"))

        manifest.update({
            "status": "ok",
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost_usd": cost,
            "files": written,
        })
        log.info(f"[green]{label}[/] done -> {len(written)} section files ({cost_line})")
    except Exception as exc:  # noqa: BLE001 -- one model's failure shouldn't kill the session
        (model_dir / "ERROR.md").write_text(f"# {label} ({provider} / {model})\n\nFAILED: {exc}\n")
        manifest.update({"status": "error", "error": str(exc)})
        log.error(f"[red]{label}[/] FAILED: {exc}")

    save_model_manifest(model_dir, manifest)


def run_metastudy_step(run_dir: Path, synthesis_model: str, synthesis_price: tuple[float | None, float | None]) -> None:
    if not any(run_dir.glob("*/*.md")):
        log.warning("No transcripts yet -- run at least one model first.")
        return

    log.info("Building metastudy...")
    result = build_metastudy(run_dir, PRIMITIVES_PATH, REFERENCE_PATH, synthesis_model)
    (run_dir / "metastudy.md").write_text(result.report)

    price_in, price_out = synthesis_price
    cost = estimate_cost(result.input_tokens, result.output_tokens, price_in, price_out)
    log.info(f"[green]Metastudy written[/] -> {run_dir / 'metastudy.md'} ({format_usd(cost)})")


def build_menu_table(model_specs: list[dict]) -> Table:
    table = Table(title="Uriam Model Profiler")
    table.add_column("#", justify="right", style="bold")
    table.add_column("Released")
    table.add_column("Label")
    table.add_column("Provider")
    table.add_column("Model")
    for i, spec in enumerate(model_specs, start=1):
        table.add_row(str(i), spec.get("released", "—"), spec["label"], spec["provider"], spec["model"])
    return table


def interactive_menu(
    config: dict,
    run_dir: Path,
    system_prompt: str,
    sections: list[tuple[str, list[str]]],
    shas: tuple[str | None, str | None],
    synthesis_model: str,
    synthesis_price: tuple[float | None, float | None],
    ollama_service: OllamaService,
) -> None:
    model_specs = sorted(config["models"], key=lambda m: m.get("released", ""), reverse=True)
    choices = [str(i) for i in range(1, len(model_specs) + 1)] + ["a", "m", "x"]
    while True:
        console.print(build_menu_table(model_specs))
        console.print("[bold]a[/] run ALL   [bold]m[/] metastudy only   [bold]x[/] quit")
        choice = Prompt.ask("Pick a model number, a, m, or x", choices=choices, show_choices=False)

        if choice == "x":
            return
        if choice == "m":
            run_metastudy_step(run_dir, synthesis_model, synthesis_price)
            continue
        if choice == "a":
            for spec in model_specs:
                run_one(spec, run_dir, system_prompt, sections, shas, ollama_service)
            continue
        run_one(model_specs[int(choice) - 1], run_dir, system_prompt, sections, shas, ollama_service)


def main() -> None:
    load_dotenv(PROFILE_DIR / ".env")

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--date", default=datetime.now().strftime("%Y%m%d"))
    parser.add_argument("--only", choices=["anthropic", "ollama"], default=None)
    parser.add_argument("--models", default=None, help="Comma-separated labels from models.yaml to run, e.g. --models haiku-4-5")
    parser.add_argument("--all", action="store_true", help="Run every configured model, non-interactively")
    parser.add_argument("--skip-metastudy", action="store_true")
    args = parser.parse_args()

    config = yaml.safe_load(MODELS_CONFIG_PATH.read_text())
    model_specs = config["models"]
    if args.only:
        model_specs = [m for m in model_specs if m["provider"] == args.only]
    if args.models:
        wanted = {label.strip() for label in args.models.split(",")}
        model_specs = [m for m in model_specs if m["label"] in wanted]
        missing = wanted - {m["label"] for m in model_specs}
        if missing:
            log.warning(f"No models.yaml entry for labels: {', '.join(sorted(missing))}")

    run_dir = PROFILE_DIR / args.date
    run_dir.mkdir(parents=True, exist_ok=True)
    shas = (git_sha_for(PRIMITIVES_PATH), git_sha_for(INSTRUCTIONS_PATH))

    system_prompt = PRIMITIVES_PATH.read_text()
    sections = parse_sections(INSTRUCTIONS_PATH)
    total_questions = sum(len(qs) for _, qs in sections)
    log.info(f"Loaded {len(sections)} sections ({total_questions} questions) from instructions.md")

    synthesis_model = config["synthesis"]["model"]
    synthesis_spec = next((m for m in config["models"] if m["model"] == synthesis_model), {})
    synthesis_price = (synthesis_spec.get("price_in"), synthesis_spec.get("price_out"))

    batch_requested = bool(args.only or args.models or args.all)
    interactive = not batch_requested and sys.stdin.isatty()
    if not interactive and not batch_requested:
        log.warning("No TTY detected -- running all configured models non-interactively.")

    ollama_service = OllamaService()
    try:
        if interactive:
            interactive_menu(config, run_dir, system_prompt, sections, shas, synthesis_model, synthesis_price, ollama_service)
        else:
            for spec in model_specs:
                run_one(spec, run_dir, system_prompt, sections, shas, ollama_service)
            if not args.skip_metastudy:
                run_metastudy_step(run_dir, synthesis_model, synthesis_price)
    except KeyboardInterrupt:
        log.warning("Interrupted.")
    finally:
        if ollama_service.started_by_us:
            ollama_service.shutdown()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Runs primitives.md / instructions.md against configured models.

Each `##` section in instructions.md becomes one conversation turn -- all of
that section's numbered questions are sent together in a single message, and
the reply is written to its own file. Each model gets its own self-contained
folder (YYYYMMDDHHMM/<provider>__<label>/), with its own manifest.json
alongside its section files -- no shared file that every model run has to
coordinate writes to. The YYYYMMDDHHMM stamp is taken once, when run.py
starts, not per model -- so every model in the same run.py invocation lands
in the same run folder, and separate invocations never collide or overwrite
each other, which keeps runs comparable over time.

No selection flags + a real terminal -> interactive menu (pick a model,
run it, repeat; 'a' for all, 'q' to quit).

Usage:
    python run.py                       # interactive menu
    python run.py --all                 # every configured model, no menu
    python run.py --only anthropic      # skip Ollama
    python run.py --models haiku-4-5    # just one, by its models.yaml label
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from rich.prompt import Prompt
from rich.table import Table
import yaml

from lib.ollama_service import OllamaService
from lib.pricing import estimate_cost, format_usd
from lib.providers import get_provider

# How many characters of the live-streamed response tail to show in the
# progress line -- a live preview of what the model is actually writing,
# not just a spinner.
LIVE_PREVIEW_CHARS = 50

PROFILE_DIR = Path(__file__).parent
PRIMITIVES_PATH = PROFILE_DIR / "primitives.md"
INSTRUCTIONS_PATH = PROFILE_DIR / "instructions.md"
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
) -> tuple[list[str], int, int, float]:
    """Runs one turn per section (that section's questions batched together),
    writing each section's transcript to its own file as soon as it
    completes -- so a later section failing doesn't lose earlier progress.

    Returns (written file names, total_input_tokens, total_output_tokens, total_elapsed_seconds).
    """
    client = get_provider(provider, model)
    messages: list[dict] = []
    total_input_tokens = 0
    total_output_tokens = 0
    total_elapsed = 0.0
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

            def on_progress(text_so_far: str) -> None:
                tail = text_so_far.replace("\n", " ").strip()[-LIVE_PREVIEW_CHARS:]
                progress.update(task, current=f"[{index}/{len(sections)}] {section} -- ...{tail}")

            turn_start = time.monotonic()
            reply = client.send(messages, system=system, on_progress=on_progress)
            elapsed = time.monotonic() - turn_start

            if reply.truncated:
                # Stop here, before this reply is saved or fed forward as
                # context: a truncated file would misrepresent the model's
                # actual answer, and appending a cut-off assistant turn would
                # corrupt every later section's conversation history with it.
                raise RuntimeError(
                    f"section {index}/{len(sections)} [{section}] hit the output token cap "
                    f"({reply.output_tokens} tokens generated) -- refusing to save a truncated "
                    f"reply or build later turns on top of incomplete context"
                )

            messages.append({"role": "assistant", "content": reply.text})

            total_input_tokens += reply.input_tokens
            total_output_tokens += reply.output_tokens
            total_elapsed += elapsed

            tok_per_sec = reply.output_tokens / elapsed if elapsed > 0 else 0
            log.info(
                f"[dim]{label}[/] {index}/{len(sections)} [{section}] -- "
                f"{reply.output_tokens} tokens in {elapsed:.1f}s ({tok_per_sec:.1f} tok/s)"
            )

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

    return written, total_input_tokens, total_output_tokens, total_elapsed


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

    # Wipe any previous run of this model in this run folder so re-picking
    # it from the interactive menu never leaves stale/mismatched files (e.g.
    # from an older instructions.md shape) sitting alongside fresh ones.
    for stale in model_dir.glob("*"):
        stale.unlink()
    model_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "run_id": run_dir.name,
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

        written, input_tokens, output_tokens, elapsed = run_model(label, provider, model, system_prompt, sections, model_dir)
        cost = estimate_cost(input_tokens, output_tokens, spec.get("price_in"), spec.get("price_out"))
        cost_line = format_usd(cost, free=(provider == "ollama"))
        avg_tok_per_sec = output_tokens / elapsed if elapsed > 0 else 0

        manifest.update({
            "status": "ok",
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost_usd": cost,
            "elapsed_seconds": elapsed,
            "avg_tokens_per_second": avg_tok_per_sec,
            "files": written,
        })
        log.info(
            f"[green]{label}[/] done -> {len(written)} section files "
            f"({avg_tok_per_sec:.1f} tok/s avg, {cost_line})"
        )
    except Exception as exc:  # noqa: BLE001 -- one model's failure shouldn't kill the session
        (model_dir / "ERROR.md").write_text(f"# {label} ({provider} / {model})\n\nFAILED: {exc}\n")
        manifest.update({"status": "error", "error": str(exc)})
        log.error(f"[red]{label}[/] FAILED: {exc}")

    save_model_manifest(model_dir, manifest)


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


def build_sections_table(sections: list[tuple[str, list[str]]]) -> Table:
    table = Table(title="Question Sets")
    table.add_column("#", justify="right", style="bold")
    table.add_column("Section")
    table.add_column("Questions", justify="right")
    for i, (name, questions) in enumerate(sections, start=1):
        table.add_row(str(i), name, str(len(questions)))
    return table


def pick_sections(sections: list[tuple[str, list[str]]]) -> list[tuple[str, list[str]]] | None:
    """Prompts once for which section(s) this whole session should run.
    Returns None if the user quit here."""
    console.print(build_sections_table(sections))
    console.print("[bold]a[/] run ALL sections   [bold]q[/] quit")
    choices = [str(i) for i in range(1, len(sections) + 1)] + ["a", "q"]
    choice = Prompt.ask("Pick a section number, a, or q", choices=choices, show_choices=False)

    if choice == "q":
        return None
    if choice == "a":
        return sections
    return [sections[int(choice) - 1]]


def interactive_menu(
    config: dict,
    run_dir: Path,
    system_prompt: str,
    sections: list[tuple[str, list[str]]],
    shas: tuple[str | None, str | None],
    ollama_service: OllamaService,
) -> None:
    selected_sections = pick_sections(sections)
    if selected_sections is None:
        return

    model_specs = sorted(config["models"], key=lambda m: m.get("released", ""), reverse=True)
    choices = [str(i) for i in range(1, len(model_specs) + 1)] + ["a", "q"]
    while True:
        console.print(build_menu_table(model_specs))
        console.print("[bold]a[/] run ALL   [bold]q[/] quit")
        choice = Prompt.ask("Pick a model number, a, or q", choices=choices, show_choices=False)

        if choice == "q":
            return
        if choice == "a":
            for spec in model_specs:
                run_one(spec, run_dir, system_prompt, selected_sections, shas, ollama_service)
            continue
        run_one(model_specs[int(choice) - 1], run_dir, system_prompt, selected_sections, shas, ollama_service)


def main() -> None:
    load_dotenv(PROFILE_DIR / ".env")

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--only", choices=["anthropic", "ollama"], default=None)
    parser.add_argument("--models", default=None, help="Comma-separated labels from models.yaml to run, e.g. --models haiku-4-5")
    parser.add_argument("--all", action="store_true", help="Run every configured model, non-interactively")
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

    run_dir = PROFILE_DIR / datetime.now().strftime("%Y%m%d%H%M")
    run_dir.mkdir(parents=True, exist_ok=True)
    shas = (git_sha_for(PRIMITIVES_PATH), git_sha_for(INSTRUCTIONS_PATH))

    system_prompt = PRIMITIVES_PATH.read_text()
    sections = parse_sections(INSTRUCTIONS_PATH)
    total_questions = sum(len(qs) for _, qs in sections)
    log.info(f"Loaded {len(sections)} sections ({total_questions} questions) from instructions.md")

    batch_requested = bool(args.only or args.models or args.all)
    interactive = not batch_requested and sys.stdin.isatty()
    if not interactive and not batch_requested:
        log.warning("No TTY detected -- running all configured models non-interactively.")

    ollama_service = OllamaService()
    try:
        if interactive:
            interactive_menu(config, run_dir, system_prompt, sections, shas, ollama_service)
        else:
            for spec in model_specs:
                run_one(spec, run_dir, system_prompt, sections, shas, ollama_service)
    except KeyboardInterrupt:
        log.warning("Interrupted.")
    finally:
        if ollama_service.started_by_us:
            ollama_service.shutdown()


if __name__ == "__main__":
    main()

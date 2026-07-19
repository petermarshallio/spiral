"""Builds the cross-model metastudy report from a completed run's transcripts."""

from __future__ import annotations

from pathlib import Path
from typing import NamedTuple

import anthropic

METASTUDY_MAX_TOKENS = 8192

PROMPT_TEMPLATE = """You are analyzing a test of how well different LLMs understand a formal \
framework called Uriam, without being told its real-world names for anything.

Below is `primitives.md` -- the abstract specification every test model was given verbatim \
as its system prompt. It deliberately uses placeholder letters (A/B/C/D for Node types, a/b/c/d \
for Edge types) instead of the framework's real stage names, to test whether a model can reason \
from the formal definitions alone.

<primitives.md>
{primitives}
</primitives.md>

Below is `reference.md` -- the canonical, complete definition of the same framework, INCLUDING \
the real names the test models were never shown (Internalising/Examining/Externalising/Interacting \
map to A/B/C/D; the Match/Mismatch and Velocity/Momentum/Stagnation definitions are identical, just \
named). Use this ONLY as your answer key for grading -- the test models never saw it.

<reference.md>
{reference}
</reference.md>

Below are full transcripts of the same test (from instructions.md), run as one continuous \
conversation per model -- one section's worth of questions per turn, reassembled here in order.

<transcripts>
{transcripts}
</transcripts>

Write a report with two parts:

## 1. Is primitives.md an unambiguous specification?

Look across every model's answers to the SAME question. Where multiple models converge on a \
consistent, correct-per-reference.md reading, that's evidence the definition is sound. Where \
models diverge, or converge on a plausible-but-wrong reading, quote the specific sentence(s) in \
primitives.md responsible and suggest a fix. Do not blame a model for a genuinely ambiguous \
definition.

## 2. Per-model capability comparison

For each model, score its performance (out of 5) on:
- Node/Edge classification accuracy (reference.md's mapping is ground truth)
- Correct application of the Match/Mismatch definitions
- Coherence and self-consistency of its own Behavior-Graph self-description
- Correct use of Velocity / Momentum / Stagnation in its own terms
- Quality of the Self-Reflection section, judged against what actually happened earlier in ITS \
OWN conversation (not against other models' conversations)

End with a ranked table and a short narrative on what separates the strongest and weakest \
performers.
"""


class MetastudyResult(NamedTuple):
    report: str
    input_tokens: int
    output_tokens: int


def build_metastudy(
    run_dir: Path,
    primitives_path: Path,
    reference_path: Path,
    synthesis_model: str,
) -> MetastudyResult:
    # Each model has its own folder (run_dir/<provider>__<label>/) containing
    # one file per section (<NN>-<slug>.md, or ERROR.md if the run failed).
    # Reassemble each model's files in order so the synthesis model sees one
    # coherent conversation per model, same as before the per-model split.
    transcript_sections = []
    for model_dir in sorted(p for p in run_dir.iterdir() if p.is_dir()):
        md_files = sorted(model_dir.glob("*.md"))
        if not md_files:
            continue
        combined = "\n\n".join(f.read_text() for f in md_files)
        transcript_sections.append(f"## Transcript: {model_dir.name}\n\n{combined}")

    prompt = PROMPT_TEMPLATE.format(
        primitives=primitives_path.read_text(),
        reference=reference_path.read_text(),
        transcripts="\n\n---\n\n".join(transcript_sections),
    )

    client = anthropic.Anthropic()
    response = client.messages.create(
        model=synthesis_model,
        max_tokens=METASTUDY_MAX_TOKENS,
        messages=[{"role": "user", "content": prompt}],
    )
    report = "".join(block.text for block in response.content if block.type == "text")
    return MetastudyResult(
        report=report,
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
    )

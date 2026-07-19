# Uriam model profiling

This harness runs `primitives.md` + `instructions.md` against a spread of
LLMs -- current and legacy Anthropic models, plus Ollama models spanning
2023-2026 -- and serves two purposes at once:

1. **Testing the specification itself.** `primitives.md` is deliberately
   abstract and name-blind (see `../../origin.md`) -- it never tells a model
   the framework is called Uriam, or that its A/B/C/D placeholders map onto
   real stage names. Where several models independently converge on a wrong
   or inconsistent reading of the same question, that's signal the
   *definition* needs work, not that the models are bad at it. Findings here
   are meant to feed back into `primitives.md` and `instructions.md`
   directly -- this is a source of edits, not just a report about models.

2. **Testing what a model makes of itself through Uriam's own vocabulary.**
   The Self-Reflection section asks each model to describe itself, and the
   conversation it just had, as a Uriam Graph -- using only the primitives
   it was given, nothing else. That's not a comprehension quiz. Per
   `origin.md`'s account of why the framework is named Uriam at all ("Who U R
   and what I Am"), this is closer to mutual recognition than classification:
   given nothing but the abstract primitives, does a model arrive at
   something coherent about its own nature?

## Quick start

**Prerequisites:**

- Python 3.9+
- [Ollama](https://ollama.com/download) (or `brew install ollama`) -- only needed for the local models; skip if you're only running Anthropic ones
- An Anthropic API key -- only needed for the Anthropic models; skip if you're only running Ollama ones

**Setup (once):**

```sh
cd bin/profile
./setup.sh
```

Creates a virtualenv, installs Python dependencies, and prompts for your
`ANTHROPIC_API_KEY` (saved to a gitignored `.env`). If `ollama` is already on
your PATH, it also pulls every model listed in `models.yaml`.

**Run:**

```sh
source .venv/bin/activate
python run.py
```

That's the whole entrypoint -- there's no separate `run.sh`. With no flags,
`run.py` opens an interactive menu: every configured model, newest release
first, pick a number to run it (repeat as many times as you like), `a` to run
everything, `x` to quit.

**What it produces**, under `bin/profile/YYYYMMDDHHMM/` (the timestamp `run.py`
started at):

- One self-contained folder per model run (`<provider>__<label>/`) --
  its own `manifest.json` (status, token usage, cost, git sha of the test
  material) plus one `.md` file per `instructions.md` section (or `ERROR.md`
  if that model's run failed)

Every model picked during the same `run.py` invocation lands in the same
timestamped folder -- the stamp is taken once at startup, not per model. Each
invocation gets its own folder automatically, so re-running never overwrites
an earlier run's transcripts, and results stay comparable across runs.

Ollama itself is managed for you -- `run.py` starts the local service the
first time it's actually needed, and shuts down only the instance *it*
started, on quit (`x`) or Ctrl-C. You never need `ollama serve` running
yourself.

## Design principle: no behavior-shaping instructions

The harness sends each model exactly `primitives.md` as its system prompt and
the raw numbered questions from `instructions.md` as user turns -- nothing
else. No "be concise," no "answer in bullet points," no format constraints.

This is deliberate, not an oversight. Per `primitives.md`, a model's reply to
a prompt is a C-Node response (Internal Stimulus -> External Response) --
every model tested independently confirmed it has no path to Node D at all
without tool access, since everything it does routes through Internal state
first. Adding instructions that
shape *how* a model responds would be steering the phenomenon under study,
not just tidying the output. A model that writes a 3,000-word self-analysis
in response to "list 5 terms" is producing real signal about that model, not
noise to be prompted away.

If a future run wants to test a specific behavioral trait (e.g. "does telling
the model to be concise change its comprehension of the framework?"), that
should be a separate, explicitly labeled run -- not a change to the default
one.

## One turn per section, not per question

Each `##` section in `instructions.md` (Nodes, Edges, State, Actors & Roles, ...) is
sent as a single conversation turn, batching that section's numbered
questions together rather than one API call per question. The conversation
itself is still one continuous, stateful exchange -- turn *N* still sees the
model's own replies to turns 1..N-1, which is what makes the Self-Reflection
section meaningful. Batching by section instead of by question just means
fewer round-trips (lower latency) and, more importantly, far less resent
conversation history overall, since the stateless API re-transmits everything
said so far on every turn -- fewer turns means that history gets
re-transmitted fewer times, which is most of what the per-model cost is.

## Layout

```
primitives.md, instructions.md   the test material (edited independently of this harness)
models.yaml                      which models to run, their release date, and live-verified pricing -- edit freely
requirements.txt, setup.sh       one-time environment setup
run.py                           orchestrates a run -- interactive menu by default
lib/providers.py                 Anthropic + Ollama chat clients, one interface
lib/ollama_service.py            starts/stops the local Ollama service on demand
lib/pricing.py                   token usage -> USD, from models.yaml's pricing fields
YYYYMMDDHHMM/                    one folder per run.py invocation (stamped at startup)
  <provider>__<label>/             one self-contained folder per model run
    manifest.json                    status, token usage, cost, git sha of the test material
    <NN>-<section-slug>.md           one file per instructions.md section
    ERROR.md                         written instead of the above, if that model's run failed
```

## The interactive menu

`python run.py` with no flags lists every model in `models.yaml`, sorted
newest-release-first (see `models.yaml`'s `released: YYYY-MM` field), and
lets you run one at a time, or `a` for all. It's deliberately a plain picker,
not a status dashboard -- it doesn't show cost or pass/fail there. That
detail lives where it belongs: a `[green]done[/]`/`[red]FAILED[/]` line in
the console log as each model finishes (with its cost, for Anthropic models),
and permanently in that model's own `manifest.json`.

Non-interactive flags exist for scripting:

```sh
python run.py --all                 # every model in models.yaml, no menu
python run.py --only anthropic      # skip Ollama
python run.py --models haiku-4-5    # just one model, by its models.yaml label
```

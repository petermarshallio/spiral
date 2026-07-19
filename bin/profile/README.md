# Uriam model profiling

Runs `primitives.md` + `instructions.md` against a spread of LLMs (current and
legacy Anthropic models, plus a handful of Ollama models spanning 2023-2024)
to see (a) whether `primitives.md` is an unambiguous specification, and (b)
how differently models actually understand it.

## Design principle: no behavior-shaping instructions

The harness sends each model exactly `primitives.md` as its system prompt and
the raw numbered questions from `instructions.md` as user turns -- nothing
else. No "be concise," no "answer in bullet points," no format constraints.

This is deliberate, not an oversight. Per `primitives.md`, a model's reply to
a prompt *is* a D Edge traversal (External Stimulus -> External Response) --
the thing this test is actually trying to observe. Adding instructions that
shape *how* a model responds would be steering the phenomenon under study,
not just tidying the output. A model that writes a 3,000-word self-analysis
in response to "list 5 terms" is producing real signal about that model, not
noise to be prompted away.

If a future run wants to test a specific behavioral trait (e.g. "does telling
the model to be concise change its comprehension of the framework?"), that
should be a separate, explicitly labeled run -- not a change to the default
one.

## One turn per section, not per question

Each `##` section in `instructions.md` (Nodes, Edges, Behavior Graph, ...) is
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
models.yaml                      which models to run, and their live-verified pricing -- edit freely
requirements.txt, setup.sh       one-time environment setup
run.py                           orchestrates a run -- interactive menu by default
lib/providers.py                 Anthropic + Ollama chat clients, one interface
lib/ollama_service.py            starts/stops the local Ollama service on demand
lib/pricing.py                   token usage -> USD, from models.yaml's pricing fields
lib/metastudy.py                 builds the cross-model synthesis report
YYYYMMDD/                        one folder per run
  manifest.json                    which models ran, cost, token usage, git sha of the test material
  transcripts/<provider>__<label>__<NN>-<section-slug>.md   one file per section per model
  transcripts/<provider>__<label>__ERROR.md                 written instead, if that model's run failed
  metastudy.md                     cross-model synthesis (skip with --skip-metastudy)
```

## Running it

```sh
./setup.sh                          # venv, deps, .env, pull Ollama models
source .venv/bin/activate
python run.py                       # interactive menu: pick a model, run it, repeat
python run.py --all                 # every model in models.yaml, no menu
python run.py --only anthropic      # skip Ollama
python run.py --models haiku-4-5    # just one model, by its models.yaml label
python run.py --skip-metastudy      # collect transcripts, skip the synthesis call
```

Ollama is managed for you -- `run.py` starts the local service the first time
it's actually needed and shuts down only the instance it started, on quit
('x') or Ctrl-C. You don't need `ollama serve` running yourself.

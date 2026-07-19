# Uriam

**A model of how any Actor — human or machine — moves from raw input to meaningful output.**

Built from a small set of primitives — Actor, Role, Node, Edge — that combine into a Behavior Graph. Any two Actors that share this model can examine their own behavior with it, or work together.

## What's in this repo

| File | Purpose |
| --- | --- |
| [`bin/profile/primitives.md`](./bin/profile/primitives.md) | The fundamentals — Actor, Role, Node, Edge, Behavior Graph. Everything else is built on this. |
| [`about.md`](./about.md) | The narrative explanation — why the framework works |
| [`reference.md`](./reference.md) | Strict definitions and lookup tables |
| [`references.md`](./references.md) | External sources the framework draws on |
| [`origin.md`](./origin.md) | The framework's history |
| [`SKILL.md`](./SKILL.md) | The operational layer — how to actually run Uriam in a live conversation |

## Test harness

[`bin/profile/`](./bin/profile/) runs the primitives against a spread of LLMs — current and legacy Anthropic models, plus local Ollama models — to check whether `primitives.md` is an unambiguous specification, and how differently models actually understand it.

- [`bin/profile/primitives.md`](./bin/profile/primitives.md) + [`bin/profile/instructions.md`](./bin/profile/instructions.md) — the test material itself
- [`bin/profile/README.md`](./bin/profile/README.md) — how the harness works, and how to run it

## Using it

There's nothing to install. Point an AI assistant at this repo (or paste in `SKILL.md`, alongside the other files if it can't read them directly) and ask it to work through Uriam with you.

Uriam requires explicit invocation — say the word to start it, no ambient auto-detection. See [`SKILL.md`](./SKILL.md) for the current invocation phrase.

## Try it now

> *"I've been thinking about going to Geneva for a holiday. I keep looking at flights and hotels but I haven't booked anything."*

Claude will identify which stage of the graph you're in, which Role you're about to meet, and what genuine forward movement looks like.

---

## Learn more

The full framework — the primitives, the matrix, the cast, the Stage Manager, and how it maps onto AI system design — is in [`about.md`](./about.md).

## License

[Creative Commons Attribution-NonCommercial 4.0 International](./LICENSE.md) (CC BY-NC 4.0)

Free to use and adapt with attribution. Commercial use requires permission.

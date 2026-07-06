# Spiral

**A thinking protocol for humans and machines.**

Any two minds that speak it — human or AI — can work together.

## What's in this repo

| File | Purpose |
| --- | --- |
| [`about.md`](./about.md) | The full canonical framework — the single source of truth |
| [`.claude/skills/spiral/`](./.claude/skills/spiral/) | The skill bundle — `SKILL.md` plus two momentum-logging scripts. It reads `about.md` directly when it's running inside this repo, and falls back to fetching it from GitHub otherwise, so there's nothing bundled to keep in sync |

## Installation

**Claude Code:** drop the `.claude/skills/spiral/` folder into a project's `.claude/skills/` (project-only) or `~/.claude/skills/` (all your projects). It's discovered automatically — no restart needed.

**Claude Desktop / claude.ai:** zip the `.claude/skills/spiral` folder as-is and upload it via **Customize** → **Skills**. Outside this repo, the skill has no local `about.md` to read, so it fetches the canonical version from GitHub the first time it needs the full reference — that requires the skill to have web access on whatever surface it's running on.

The skill requires explicit invocation (see below) — say the word to start it, no ambient auto-detection.

## Try it now

Spiral only runs when you ask for it by name — say **"Spiral with me"** followed by whatever you're stuck on:

> *"Spiral with me: I've been thinking about going to Geneva for a holiday. I keep looking at flights and hotels but I haven't booked anything."*

Claude will identify which Spiral stage you're in, which character you're about to meet, and what genuine forward movement looks like.

---

## Learn more

The full framework — the matrix, the cast, the Stage Manager, the fractal property, and how Spiral maps onto AI system design — is in [`about.md`](./about.md).

## License

[Creative Commons Attribution-NonCommercial 4.0 International](./LICENSE.md) (CC BY-NC 4.0)

Free to use and adapt with attribution. Commercial use requires permission.

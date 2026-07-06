# Spiral

**A thinking protocol for humans and machines.**

Any two minds that speak it — human or AI — can work together.

---

## What's in this repo

| File | Purpose |
| --- | --- |
| [`about.md`](./about.md) | The full canonical framework |
| [`.claude/skills/spiral/`](./.claude/skills/spiral/) | The skill bundle — `SKILL.md`, a `reference.md` link to `about.md`, and two momentum-logging scripts |

---

## Installation

**Claude Code:** drop the `.claude/skills/spiral/` folder into a project's `.claude/skills/` (project-only) or `~/.claude/skills/` (all your projects). It's discovered automatically — no restart needed.

**Claude Desktop / claude.ai:** the bundle needs to travel as a self-contained zip, and `reference.md` is a symlink in this repo (it just points at `about.md`, so there's one source of truth instead of two copies to keep in sync). Zip tools don't reliably preserve symlinks, so resolve it into a real file first, in a copy — not in place:

```bash
cp -RL .claude/skills/spiral /tmp/spiral-skill   # -L follows the symlink into a real file
cd /tmp && zip -r spiral-skill.zip spiral-skill
```

Then **Customize** → **Skills** → upload `spiral-skill.zip`.

The skill requires explicit invocation (see below) — say the word to start it, no ambient auto-detection.

---

## Try it now

Spiral only runs when you ask for it by name — say **"Spiral with me"** followed by whatever you're stuck on:

> *"Spiral with me: I've been thinking about going to Geneva for a holiday. I keep looking at flights and hotels but I haven't booked anything."*

Claude will identify which Spiral stage you're in, which character you're about to meet, and what genuine forward movement looks like.

---

## Learn more

The full framework — the matrix, the cast, the Stage Manager, the fractal property, and how Spiral maps onto AI system design — is in [`about.md`](./about.md).

---

## License

[Creative Commons Attribution-NonCommercial 4.0 International](./LICENSE.md) (CC BY-NC 4.0)

Free to use and adapt with attribution. Commercial use requires permission.

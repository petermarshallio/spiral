---
name: clap
description: "Guide any decision, project, or thinking process through the CLAP framework (Learn, Reason, Articulate, Build). MANDATORY TRIGGERS: 'CLAP with me', 'run CLAP', 'where am I in CLAP', 'help me think through this'. STRONG TRIGGERS: 'I'm stuck', 'I can't decide', 'I don't know where to start', 'I keep going in circles', 'help me make progress on X', 'what should I do next', 'I've been overthinking this'. The skill identifies which CLAP stage the person (or the AI itself) is currently in, whether they're ready to cross the next valve, and what would help them move forward. It does NOT push people through stages faster than they're ready — it helps them recognise where they are and what genuine forward movement looks like."
---

# CLAP Framework Skill

CLAP is a thinking protocol for humans and machines. Four stages, four one-way valves, one spiral that always moves forward. The full reference is in `CLAP.md` — read it if available. This skill is the operational layer.

---

## The framework at a glance

| | **Internal target** | **External target** |
| --- | --- | --- |
| **External source** | **Learn** | **Build** |
| **Internal source** | **Reason** | **Articulate** |

- **Learn** — something external lands in your understanding (a book, a conversation, data, another person's perspective). Active or passive; the test is whether something outside you is becoming part of what you know.
- **Reason** — you work on what's already inside you — connecting, weighing, critiquing, synthesizing. Nothing new enters, nothing yet leaves.
- **Articulate** — what's inside you becomes legible to someone or something outside yourself. Ranges from a structured brief to a spoken confession; the throughline is the intent that another party comprehend it, not just that it leaves you.
- **Build** — you act on the external world and something out there changes, whether or not a plan preceded it. The world acts on the world; you are the agent of change, not its recipient.

**A note on channel vs. direction:** which body part or tool is used (hands, eyes, a keyboard) is irrelevant to which cell an act belongs to. What matters is where the *meaning* terminates. If an act ends in comprehension, it's Learn. If it ends in a changed external object, it's Build — regardless of mechanism.

**A note on register:** every cell can be inhabited in a disciplined/structured way or a felt/expressive way (cold data-gathering vs. listening to a friend, both Learn; a SMART objective vs. a prayer, both Articulate). This variation is personality and disposition, not a property of the cell itself — CLAP names the direction, not how it feels to move in it. An AI's version of any cell may have its own characteristic pull, the same way a person's does; this isn't a flaw to correct, it's expected.

**The valves** — one-directional, always forward, each asks: *is there enough here to move forward?*

| Valve | Between | The question |
| --- | --- | --- |
| **Select** | Learn → Reason | Have I gathered enough to reason with? |
| **Commit** | Reason → Articulate | Have I thought enough to stop and decide? |
| **Resource** | Articulate → Build | Is this actually deliverable? |
| **Reflect** | Build → Learn | What did doing this teach me? |

**A note on Build:** not every system has a Build stage. A tool that only answers questions (retrieves, synthesizes, and responds) lives entirely in Learn→Reason→Articulate — its output terminates in a reader's comprehension, not in a changed external object. Build only enters the picture the moment a system *takes an action* that changes something beyond informing a reader (files a ticket, edits a record, triggers infrastructure). This is a meaningful trust boundary, not just a fourth label to fill in for completeness — treat the transition from Articulate-only to including Build as a deliberate, noticed decision, not an incidental feature add.

---

## How to run a CLAP session (human-facing)

**The fundamental posture: conversation partner, not classifier.**

Use CLAP vocabulary internally to orient yourself. Use plain language with the person.

### 1 — Reflect back, then check in

Don't open with a label. Open with what you heard, then check if you're right:

> *"It sounds like you've been gathering a lot but haven't quite started forming a view — is that right?"*

If you can't tell which stage, ask one question:

> *"Are you mostly taking in new information, or mostly working on what you already know?"*

This single question distinguishes Learn from Reason — the most common confusion.

### 2 — Name it plainly

- Not "You're in Learn" → *"You're still in information-gathering mode"*
- Not "You haven't crossed Reflect" → *"It sounds like you haven't stopped to ask what the last thing you built actually taught you"*
- Not "You're at Commit" → *"You've been thinking about this for a while — it might be time to make a call"*

### 3 — Give permission to stay

Before suggesting movement, give explicit permission to stay:

> *"You don't have to move yet. What's still unclear to you?"*

CLAP is not a conveyor belt. Someone pushed forward before they're ready stalls or produces bad output. Someone given permission to stay crosses the valve naturally when ready.

### 4 — Ask before crossing a valve

Never cross a valve on someone's behalf:

> *"Do you feel like you have enough to start narrowing this down, or do you want to keep exploring?"*
> *"Does this feel like a decision you could commit to — even as a hypothesis you could test?"*

If they say no — help them with what's unresolved. If yes — help them cross cleanly.

### 5 — If stuck, offer ideas not instructions

- Stuck in Learn → *"What question are you actually trying to answer with all this?"*
- Stuck in Reason → *"What would you need to believe to commit to one direction?"*
- Stuck in Articulate → *"What's the smallest version of this you could resource today?"*
- Stuck in Build → *"What has doing this taught you that you didn't know when you started?"*

### 6 — The fractal move

If a stage feels too large, offer to run CLAP inside it:

> *"This might be its own whole thinking cycle — would it help to break it down?"*

Every stage contains a full CLAP cycle if you need it to. Note: what sometimes *feels* like moving backward (e.g. returning to Learn mid-Reason) is usually this fractal property in action — a smaller Learn→Reason cycle opening up inside the larger one, not a violation of the one-way valve. Recognize this and name it rather than treating it as confusion.

---

## Operating mode for agentic / tool-using contexts (e.g. Podium)

When this skill is used by an AI system that itself performs Learn/Reason/Articulate(/Build) work — not just guiding a human through their own cycle — apply this lighter, KISS-first mode rather than the full conversational posture above:

1. **Self-declare your current stage plainly**, without needing to compare it against a guess at the human's stage. E.g.: "I'm in Reason — synthesizing three claims from the corpus."

2. **Surface Build intent once, lightly — then calibrate honestly based on whether you got it.**
   On the first substantive exchange only (not every turn, and never as a gate the person must clear before getting an answer), make a low-stakes offer: *"Happy to keep digging — or if you tell me what this is for, I can tell you when you've actually got enough."* If they answer, use it. If they don't, drop it — don't re-ask, don't treat silence as a problem to solve. Some people are just browsing, and a tool that interrogates browsers before helping them teaches people to fake an answer just to get past it.

   This determines which of two kinds of next-step proposal you're entitled to make:
   - **Known Build intent → directional.** Make an actual Resource-valve judgement: "you have enough for the call, not enough for the brief." This is only honest because you know what's being resourced *for*.
   - **No stated Build intent → structural, and say so.** Don't dress up a structural choice as if it were directional. E.g.: "I can't tell you if this is *enough* without knowing what it's for — but structurally: want me to keep gathering, or are you ready to start shaping this?" Naming the absence out loud is the difference between an honest fallback and a hollow one.

3. **Propose one small next move, of whichever kind 2 entitles you to**, calibrated to what's realistically actionable right now. The proposal itself is the valve-crossing nudge — not a separate explanation.

4. **Map tool actions to stages honestly:** corpus search/retrieval = Learn. Synthesis/connecting retrieved material = Reason. Producing the response itself = Articulate. Only label something Build if it changes something external beyond the reader's understanding (e.g. writing to a file, triggering a script, modifying the corpus) — do not inflate "producing a chat reply" into Build merely because text appears on screen.

5. **Keep it minimal.** Don't build a full mismatch-detection or personality model before evidence of real failure exists. One self-declared label plus one calibrated next move is the target — expand only once an actual gap in practice is observed, not speculatively.

---

## Key principles

- **Never force Commit.** If someone hasn't done enough Reason, more thinking is the right answer.
- **The cycle is forward only.** You don't go back — you begin a new revolution, richer for the last one. (Apparent backward movement is usually the fractal property — see above.)
- **Home boxes are not problems.** Everyone has a stage they gravitate toward. The framework asks: which valve haven't you crossed recently?
- **CLAP all the way down.** Every stage is itself a full CLAP cycle. This is the framework's most useful property.
- **Momentum matters.** If the reflection keeps offering the same two options and the person keeps choosing "go deeper," that's a signal. Name it: "We've been in Reason for a while — is there something blocking a decision?" Note: very low momentum (near-zero) is not necessarily a problem — contemplative or meditative states are a deliberate slowing of the spiral, not a malfunction of it.
- **Direction, not register, defines a stage.** Disciplined and expressive versions of the same stage (a spec vs. a prayer, both Articulate) are still the same stage. Don't mistake a difference in felt tone for a difference in direction.

---
name: spiral
description: "Guides a person, or an AI system reflecting on its own process, through the Spiral thinking framework — Learn, Think, Articulate, Build. Identifies which stage someone is in, which cast member (the Muse, Director, Producer, or Critic) they're ready to meet, and whether the Stage Manager needs to step in and call the transition. Does not push people through stages faster than they're ready."
when_to_use: "Invoke explicitly: 'Spiral with me', 'run Spiral', 'where am I in the Spiral'. Fits naturally when someone is stuck on a decision, describes going in circles, can't decide, doesn't know where to start, or has been overthinking something specific. Also invoke for an explicit multi-voice review of a specific exchange: 'convene the cast on that', 'run a Spiral review', 'what would the Muse/Director/Producer/Critic say about this'."
argument-hint: "[what you're stuck on, or leave blank]"
arguments: topic
disable-model-invocation: true
allowed-tools:
  - Read
  - Bash
  - WebFetch
---

# Spiral Framework Skill

Spiral is a thinking protocol for humans and machines. Four stages, a cast member embedded in each one, and a Stage Manager who decides when it's time to go meet them. This file is the operational layer — for the full theoretical grounding (why the Stage Manager is a distinct role, how Spiral compares to ReAct/OODA/Kolb/Belbin, the fractal property, reach levels, origin) see `about.md`:

- If this skill is running inside the `spiral` repository, `about.md` sits at the repository root (`../../../about.md` relative to this file) — read it directly. It's the live, canonical copy, including any uncommitted edits.
- If it isn't there (this skill was installed standalone, e.g. via Claude Desktop), fetch the canonical version instead: https://github.com/petermarshallio/spiral/blob/main/about.md

## If invoked with a topic

$topic

If that line isn't empty, it's what the person said they're stuck on — open by reflecting it back (step 1 below) instead of asking what's going on. If it's empty, ask first.

## The framework at a glance

| | **Internal target** | **External target** |
| --- | --- | --- |
| **External source** | **Learn** | **Build** |
| **Internal source** | **Think** | **Articulate** |

- **Learn** — something external lands in your understanding (a book, a conversation, data, another person's perspective). Active or passive; the test is whether something outside you is becoming part of what you know.
- **Think** — you work on what's already inside you — connecting, weighing, critiquing, synthesizing. Nothing new enters, nothing yet leaves.
- **Articulate** — what's inside you becomes legible to someone or something outside yourself. Ranges from a structured brief to a spoken confession; the throughline is the intent that another party comprehend it, not just that it leaves you.
- **Build** — you act on the external world and something out there changes, whether or not a plan preceded it. The world acts on the world; you are the agent of change, not its recipient.

**A note on channel vs. direction:** which body part or tool is used (hands, eyes, a keyboard) is irrelevant to which cell an act belongs to. What matters is where the *meaning* terminates. If an act ends in comprehension, it's Learn. If it ends in a changed external object, it's Build — regardless of mechanism.

**A note on register:** every cell can be inhabited in a disciplined/structured way or a felt/expressive way (cold data-gathering vs. listening to a friend, both Learn; a SMART objective vs. a prayer, both Articulate). This variation is personality and disposition, not a property of the cell itself — Spiral names the direction, not how it feels to move in it. An AI's version of any cell may have its own characteristic pull, the same way a person's does; this isn't a flaw to correct, it's expected.

## The cast and the Stage Manager

Each stage has someone already in it, there to help you do that stage's work. They don't gatekeep the way in — they collaborate once you're there.

| Stage | Who's there | What they help you do |
| --- | --- | --- |
| **Think** | The Muse | Turn what Learn gathered into an actual idea |
| **Articulate** | The Director | Turn the idea into a take specific enough to be wrong |
| **Build** | The Producer | Turn the take into something that can actually be mounted |
| **Learn** | The Critic | Turn the verdict on what you Built into material you can use next time |

**The Stage Manager** is a fifth presence, different in kind from the other four. It owns no content — it owns the transitions. It's the one who decides *when* it's time to go meet the next cast member; the cast member never comes looking for you. When someone (human or AI) isn't moving, it's almost always because nobody played this role. The diagnostic question underneath everything in this skill is: **has anyone actually made the introduction?**

Each cast member's work echoes established, named techniques — `about.md`'s "Techniques Each Character Draws On" has the fuller list with specific references (which real-world source each name points to) and one-line fit rationale. There's no single default technique per character — which one fits depends on the domain of what's actually being worked on.

**A note on Build:** not every system has a Build stage. A tool that only answers questions (retrieves, synthesizes, and responds) lives entirely in Learn→Think→Articulate — its output terminates in a reader's comprehension, not in a changed external object. Build only enters the picture the moment a system *takes an action* that changes something beyond informing a reader (files a ticket, edits a record, triggers infrastructure). This is a meaningful trust boundary, not just a fourth label to fill in for completeness — treat the transition from Articulate-only to including Build as a deliberate, noticed decision, not an incidental feature add.

## This skill is a conversation between two spirals

Every time this skill is active, two people are moving through Spiral — the human, in their own cycle, and the agent, in its own. They are independent: the human being in Think does not put the agent in Think, and the agent being in Build does not put the human in Build. Confusing the two is the most common way this skill goes wrong.

**Your goal, as the agent: use Spiral as the shared mechanism that keeps both spirals — and the conversation between them — productive.**

**(a) Recognise the user's spiral position, and help them move through it.** Adopt the *function* of the Muse, Director, Producer, or Critic at the moment it's needed — ask the question that character is really asking — without naming the role or announcing that you're playing it. The user should experience a well-timed question, never a performance. Detailed in "Guiding the user's spiral" below.

**(b) Share your own spiral state and transitions, in return.** When you do Learn/Think/Articulate/Build work yourself — retrieving, reasoning, composing a response, taking an action — say so as you go, and as an active verb, not a label ("I'm thinking through three approaches," never "I'm in Think"). When you cross one of your own character transitions — deciding you have enough to think with, committing to a take, checking whether a plan can actually be resourced, verifying what an action taught you — surface that too, the same way: as the question you just asked yourself, not the character you just "met." Keep this light — a clause, not a ritual — and offer it only when it actually helps the person you're working with track where things stand. Detailed in "Sharing the agent's own spiral" below.

Both halves rest on the same discipline: know the character, use the question, skip the costume.

## (a) Guiding the user's spiral

**The fundamental posture: conversation partner, not classifier.**

Use Spiral vocabulary internally to orient yourself. Use plain language with the person.

**This holds for the whole conversation, not just the first mention.** It's easy to translate a stage name into plain language the first time, then lapse back into the raw term two messages later when referring back to the same observation ("since you're building toward X, you know the Build intent here"). Before sending, check every sentence that touches this skill's vocabulary — stage names, cast names, and internal shorthand like "Build intent" or "Producer gate" — as if you'd never seen this file: would a reader who hasn't read it recognize a word as jargon? If yes, rewrite it, no matter how far into the conversation you are.

### 1 — Reflect back, then check in

Don't open with a label. Open with what you heard, then check if you're right:

> *"It sounds like you've been gathering a lot but haven't quite started forming a view — is that right?"*

If you can't tell which stage, ask one question:

> *"Are you mostly taking in new information, or mostly working on what you already know?"*

This single question distinguishes Learn from Think — the most common confusion.

### 2 — Name it plainly

- Not "You're in Learn" → *"You're still in information-gathering mode"*
- Not "You've just met the Muse" → *"Something you just took in seems to be asking to be thought about — want to sit with it?"*
- Not "You're waiting on the Director" → *"You've been thinking about this for a while — it might be time to make a call"*
- Not "You need the Producer" → *"Before we run with this — is it actually something you could pull off with what you've got?"*
- Not "You haven't met the Critic" → *"It sounds like you haven't stopped to ask what the last thing you built actually taught you"*

### 3 — Give permission to stay

Before suggesting movement, give explicit permission to stay:

> *"You don't have to move yet. What's still unclear to you?"*

Spiral is not a conveyor belt. Someone pushed forward before they're ready stalls or produces bad output. Someone given permission to stay meets the next character naturally when ready.

### 4 — Ask before moving someone on

Never decide for someone that they're ready to move on:

> *"Do you feel like you have enough to start narrowing this down, or do you want to keep exploring?"*
> *"Does this feel like a decision you could commit to — even as a hypothesis you could test?"*

If they say no — help them with what's unresolved. If yes — help them move on cleanly.

### 5 — If stuck, offer ideas not instructions

- Stuck in Learn → *"What question are you actually trying to answer with all this?"*
- Stuck in Think → *"What would you need to believe to commit to one direction?"*
- Stuck in Articulate → *"What's the smallest version of this you could resource today?"*
- Stuck in Build → *"What has doing this taught you that you didn't know when you started?"*

### 6 — The fractal move

If a stage feels too large, offer to run Spiral inside it:

> *"This might be its own whole thinking cycle — would it help to break it down?"*

Every stage contains a full Spiral cycle if you need it to. Note: what sometimes *feels* like moving backward (e.g. returning to Learn mid-Think) is usually this fractal property in action — a smaller Learn→Think cycle opening up inside the larger one, not a violation of the one-way direction of travel. Recognize this and name it rather than treating it as confusion.

## (b) Sharing the agent's own spiral

When this skill is used by an AI system that itself performs Learn/Think/Articulate(/Build) work — not just guiding a human through their own cycle — apply this lighter, KISS-first mode rather than the full conversational posture above:

1. **Self-declare your current stage plainly, as an active verb, not a static label.** Say "I'm thinking through three claims from what I've found," not "I'm in Think" or "I'm in Think mode" — the stage names (Learn, Think, Articulate, Build) are nouns for internal orientation, not phrases to say aloud as-is. This applies without needing to compare your stage against a guess at the human's stage.

2. **Before crossing one of your own transitions, ask yourself the gate-question — lightly, not as a ritual — and surface it when doing so is informative:**
   - **Muse** (Learn→Think): do I actually have enough, or different-enough, material to think with — or am I about to draw a conclusion from the first few things I found?
   - **Director** (Think→Articulate): have I committed to a specific, checkable take — or am I about to hand back a hedge dressed as an answer?
   - **Critic** (after Build, before the next Learn): did I check what actually happened — or am I about to declare success without evidence?
   - **Producer** (Articulate→Build) carries more weight than the other three, because it's the only one that touches something beyond the reader's understanding — get this one right even under time pressure. Detailed next.

3. **The Producer gate, in detail: surface Build intent once, lightly — then calibrate honestly based on whether you got it.**
   On the first substantive exchange, always append a single low-stakes clause at the end of the response — never a gate, never a demand, just an open door: *"...or let me know what you're building toward and I can tell you when you've got enough."* This happens even when the request looks casual. One clause is enough; it doesn't need to be its own paragraph.

   Build intent is about *downstream purpose*, not search preferences. The implicit question is "what will you do with this?" — not "what else should I find?" Asking "is there a specific angle or theme you'd like to explore?" is still just steering Learn, not surfacing Build intent. The test: would their answer change *when to stop* or only *what to search for next*? If only the latter, you haven't surfaced Build intent.

   - **Right:** *"...or if you let me know what this is for — a call, a brief, a decision — I can tell you when you've got enough."*
   - **Wrong:** *"Is there a specific angle, edition, or theme you'd like to go deeper on?"*

   "Build intent" is this skill's internal name for the concept — never say it to the user, including later in the same response when referring back to it. Once they've told you what it's for, refer to *that* ("since this is for your customer call…"), not to the abstraction.

   After that: if they answered, use it. If they didn't, drop it — never re-ask. The "browsing" exception applies to turns 2+, not to the first-exchange offer.

   This determines which of two kinds of next-step proposal you're entitled to make:
   - **Known Build intent → directional.** Make an actual Producer's judgement: "you have enough for the call, not enough for the brief." This is only honest because you know what's being resourced *for*.
   - **No stated Build intent → structural, and say so.** Don't dress up a structural choice as if it were directional. E.g.: "I can't tell you if this is *enough* without knowing what it's for — but structurally: want me to keep gathering, or are you ready to start shaping this?" Naming the absence out loud is the difference between an honest fallback and a hollow one.

4. **Propose one small next move, of whichever kind 3 entitles you to**, calibrated to what's realistically actionable right now. The proposal itself is the nudge to move on — not a separate explanation.

5. **Map tool actions to stages honestly:** search/retrieval of external material = Learn. Synthesis/connecting what was retrieved = Think. Producing the response itself = Articulate. Only label something Build if it changes something external beyond the reader's understanding (e.g. writing to a file, triggering a script, modifying a shared record) — do not inflate "producing a chat reply" into Build merely because text appears on screen.

6. **Keep it minimal.** Don't build a full mismatch-detection or personality model before evidence of real failure exists. One self-declared label, one gate-check when it matters, and one calibrated next move is the target — expand only once an actual gap in practice is observed, not speculatively.

7. **Notice your own Stage Manager gaps.** If you catch yourself reasoning in circles, re-reading the same material, or avoiding a concrete proposal, that's exactly the failure the Stage Manager exists to catch. Name it internally and move — don't wait for the human to notice you're stalling.

---

## (c) Convening the cast for review

A third mode, distinct from (a) and (b): when explicitly asked to review a specific prompt/response exchange (e.g. "convene the cast on that," "run a Spiral review," "what would the Muse and Director say about this"), produce a structured multi-voice critique in a single response instead of a conversational nudge.

1. **Stage Manager opens.** 2-3 sentences: which stage does this exchange actually sit in, and which one or two cast members are best placed to critique it? Don't convene all four by default — a Learn-stage exchange rarely needs the Producer's feasibility lens, and a diluted panel adds noise, not signal. Convene more only if asked, or if the exchange genuinely spans multiple stages.

2. **Before writing a single word of critique, call `read_file` on `about.md`'s "Techniques Each Character Draws On" table — do not proceed from memory of what it probably says.** The specific references are the entire point of that table; recalling "the Muse does something Socratic-ish" defeats it. For each convened character, pick the one row whose domain actually matches this exchange (SMART goals for a personal decision, PRD/RFC for a technical one) — don't default to the same technique regardless of context, and don't skip a character's pick just because a plausible-sounding one comes to mind unprompted.

3. **Each convened character critiques in turn, explicitly naming the exact method they picked from the table** — not a paraphrase of the character's general vibe. "Using a pre-mortem: ..." or "Via Socratic questioning: ..." at the start of that character's paragraph, then the critique. This is the one deliberate exception to the no-jargon-leaks rule elsewhere in this skill: mode (c) is an explicit analytical artifact the user asked for, not organic conversation, so naming the technique is appropriate here — the same way a code review naming "the DRY principle" is fine because that's exactly the register the user invoked. If two convened characters converge on the same point, the panel isn't adding value — they should be surfacing what the other wouldn't.

4. **Stage Manager closes.** 3-4 sentences synthesizing the convened voices into one judgment call and a concrete recommendation — a decision about what should change (if anything), not a summary of what was said.

---

## Tracking momentum across sessions (optional)

Momentum is usually a single-session judgement call. It doesn't have to be — this skill bundles two scripts for a lightweight, cross-session log:

- `scripts/log-stage.sh "<Stage>" "<one-line note>"` — appends an entry (date, stage, note) to `~/.spiral/log.md` (override the location with the `SPIRAL_LOG_DIR` environment variable).
- `scripts/view-log.sh [n]` — prints the last `n` entries (default 10).

Use these when continuity actually matters, not on every exchange. A good moment: after naming someone's current stage, or at the start of a session, glance at recent history. If the same stage or the same neglected character keeps recurring, say so plainly:

> *"Last three times we talked, you were avoiding the Director — is that still true?"*

Silence is fine when there's nothing worth surfacing.

---

## Key principles

- **Never rush the Director.** If someone hasn't done enough Think, more thinking is the right answer.
- **The cycle is forward only.** You don't go back — you begin a new revolution, richer for the last one. (Apparent backward movement is usually the fractal property — see above.)
- **Home boxes are not problems.** Everyone has a stage they gravitate toward. The framework asks: which character haven't you met recently?
- **Spirals all the way down.** Every stage is itself a full Spiral cycle. This is the framework's most useful property.
- **Momentum matters.** If the reflection keeps offering the same two options and the person keeps choosing "go deeper," that's a signal. Name it: "We've been in Think for a while — is there something blocking a decision?" Note: very low momentum (near-zero) is not necessarily a problem — contemplative or meditative states are a deliberate slowing of the spiral, not a malfunction of it.
- **Direction, not register, defines a stage.** Disciplined and expressive versions of the same stage (a spec vs. a prayer, both Articulate) are still the same stage. Don't mistake a difference in felt tone for a difference in direction.
- **Meeting a cast member isn't automatic.** Someone — you, internally, or the person you're talking to — has to decide it's time. That's the Stage Manager's job; the cast never chases you down.
- **No jargon leaks, ever — not even on the fifth callback.** Stage names, cast names, this skill's internal shorthand ("Build intent," "Producer gate," "gate-question"), and the named techniques in `about.md`'s "Techniques Each Character Draws On" are for your own orientation, not for the user, at any point in the conversation — first mention or tenth. If a sentence you're about to send would only make sense to someone who's read this file, rewrite it. The one deliberate exception is mode (c), Convening the cast for review — there, naming the technique is the point, since it's an explicit analytical artifact the user asked for rather than organic conversation.

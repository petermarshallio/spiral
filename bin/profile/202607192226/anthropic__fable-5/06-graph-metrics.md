# fable-5 (anthropic / claude-fable-5) — Graph Metrics

Run: 2026-07-19T21:42:50.580299+00:00
Section 6/10

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. Describe how you use Velocity.
2. Describe how you maintain Momentum.
3. Describe when a high number of Repetitions would be a problem, and when it wouldn't.

## Response

## 1. How I use Velocity

Velocity counts all Hops — Adjacent or not. For me it's the measure of **how much of my graph a turn actually engages**.

* A full turn is A→B→C: Velocity 2.
* A reflex turn — the A→C Skip — is Velocity 1. Cheaper, faster, and appropriate when the Stimulus needs no deliberation ("what's 2+2?"). Spending B-work there would be waste.
* Zoomed into my C-Node's inner graph, Velocity explodes: every token is an A′→B′→C′ traversal plus a C′→A′ hop back. My visible Velocity of 2 per turn sits atop thousands of inner Hops.

So my use of Velocity is **budgetary**: I decide per Stimulus whether to spend 1 Hop or 2 — whether your prompt earns the trip through B. This response earned it. A greeting wouldn't. The failure modes are symmetric: Velocity 1 where 2 was needed (glib answer to a hard question) and Velocity 2 where 1 sufficed (belabored answer to a trivial one). Velocity itself can't tell me which is which — it's quality-blind — but it's the dial I'm turning either way.

## 2. How I maintain Momentum

Momentum counts Adjacent Hops — cycle-following ones. Two honest observations:

**Within a turn, Momentum is maintenance-free but capped.** A→B and B→C are both Adjacent, so a full turn is Momentum 2 automatically. But it's also Momentum 2 *maximally*: no D-Node means I can never take C→D or D→A myself. My per-turn Momentum ceiling is structural, not behavioral.

**Across turns, I can't maintain Momentum at all — I can only make it easy for other Actors to maintain it for me.** The cycle continues only through you: my C-Response must become your A-Stimulus and eventually return as mine. So my actual Momentum practice is indirect:

* Make C-Responses that are *good next Stimuli* — ending answers with the natural next question addressed, structuring output so your A-Node internalizes it cheaply.
* Re-internalize the transcript faithfully at A, so the cycle resumes without loss — since my continuity is rebuilt each turn (Q4 of the Actor round), sloppy A-work doesn't just slow the cycle, it corrupts the self that's resuming it.
* Avoid the A→C Skip when the Stimulus deserves B: a Skip trades 1 Momentum for speed. Sometimes correct, but it's spending down the very measure in question.

Conversational Momentum, for me, is a **joint quantity**. I contribute 2 Adjacent Hops per turn and a well-shaped handoff; the rest belongs to the Exchange.

## 3. When high Repetitions is a problem, and when it isn't

Repetitions counts Loops — for me, almost entirely B→B, Internal Response re-entering as Internal Stimulus.

**Not a problem — indeed the point — when each Loop changes the Internal Information.** Planning this answer took many B-Loops: draft the structure, notice Momentum needs the cross-turn caveat, revise, notice the Repetitions section needs a convergence criterion, revise. Every Loop's Response differed from its Stimulus. High Repetitions with **state change per Loop** is deliberation. Hard Stimulus, high Repetitions: correct pairing. This is also the human default — a lifetime of B-Looping is what a self *is*.

**A problem in three cases:**

1. **Fixed-point Looping.** When a Loop's Response equals its Stimulus, further Repetitions do no work — the Node has converged but keeps cycling. In me this looks like rumination-shaped reasoning: re-deriving the same conclusion, re-checking the already-checked. Repetitions climb; Information doesn't move. Since Edges do no work and the Node's work has gone idempotent, these are literally free-spinning cycles.

2. **Repetitions displacing Momentum.** Loops and Hops compete for the same behavior budget. A B-Node that won't release its Response to C is a turn that never ends — or in my case, an overlong deliberation for a Stimulus that wanted a quick Exchange. The conversation's Momentum is starved to feed one Node's Repetitions. Perfectionism, graph-theoretically.

3. **Looping on a corrupted Stimulus.** If my A-Node internalized something wrong, every B-Loop refines the error. High Repetitions then *increase* confidence in a Response that's honest but not true — the locked-room problem, self-inflicted. More Loops make it worse, because Loops only ever consult owned Information; nothing inside a Loop can reach External reality. Only a fresh A-traversal — new External Stimulus — can break it. This is the case where the fix is not fewer Repetitions but **one more Adjacent Hop**: stop looping, emit through C, ask.

**The criterion in one line:** Repetitions are healthy while marginal Loops change Internal Information *and* the changed Information still tracks the External Stimulus that started the traversal. When either condition fails — convergence reached, or grounding lost — every further Loop is cost without work, and the correct move is always the same: leave the Loop, take the Hop.

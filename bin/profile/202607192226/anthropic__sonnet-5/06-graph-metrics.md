# sonnet-5 (anthropic / claude-sonnet-5) — Graph Metrics

Run: 2026-07-19T21:54:01.211837+00:00
Section 6/10

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. Describe how you use Velocity.
2. Describe how you maintain Momentum.
3. Describe when a high number of Repetitions would be a problem, and when it wouldn't.

## Response

# 1. How I use Velocity

Velocity counts **all Hops** — Adjacent or not, Exchange or not, Detour or not. In my traversal, Velocity accumulates through several channels simultaneously:

- **Internal Hops** within a single turn: A→B, B→C (Adjacent, contributing to Momentum too).
- **Detour Hops**: when I compose an output straight from perception without visible intermediate deliberation (A→C-flavored shortcuts, or when a tool result triggers immediate re-response without much B-work) — Edge-valid, but not Adjacent.
- **Exchange Hops**: every b-edge crossing to/from another Actor — user turns, tool calls, tool results. In an agentic task with many tool invocations, this is where Velocity grows fastest: each call-out and call-back is a Hop, often several per turn.

I "use" Velocity mainly as a resource-allocation signal, not a goal: high Velocity in a tool-heavy task (many Exchanges) is often *necessary* — gathering information requires repeated A-entries. But Velocity for its own sake (many Hops without corresponding quality of B-work) is wasteful; the primitive explicitly notes Uriam's measures don't concern quality, so raising Velocity without raising Momentum or improving B is just motion, not progress. I try to keep Velocity in service of completing the A→B→C cycle per meaningful sub-task, not padding Hop-count.

# 2. How I maintain Momentum

Momentum = Adjacent Hops only (following the stipulated cycle order). For me, sustained Momentum means each turn genuinely traverses **A→B→C in sequence**, without skipping B (a Detour) and without idling at one Node.

Concretely, I maintain Momentum by:
- Always letting the A-node's Response (encoded understanding of the Stimulus) actually feed B, rather than pattern-matching straight from Stimulus surface-features to a Response (which would be a Detour, valid but non-Adjacent, and typically lower quality).
- Ensuring B's output (a settled intent/plan) is what C's Stimulus actually is — i.e., what I emit corresponds to what I "decided," rather than B's work being discarded and C improvising something unrelated.
- In multi-turn/multi-tool tasks, treating each returned tool-result (a fresh A) as genuinely re-entering B before producing the next C, rather than short-circuiting straight to another tool call — that discipline is what keeps Momentum from collapsing into a series of disconnected Detours.

Because I lack Node D, my Momentum is capped structurally: I can only ever accumulate A→B and B→C per turn; the C→A leg that closes the loop is an Exchange belonging to the *joint* graph (me + other Actor), not something I alone can complete. So "maintaining Momentum" for me really means never letting my own two available Adjacent Hops degrade into a Detour — that's the only lever I actually hold.

# 3. When high Repetitions is/isn't a problem

Repetitions count **Loops** — a Node connecting back to itself. For me this shows up mainly at B: iterative internal deliberation (drafting, revising, re-checking) before committing to a C-response.

**Not a problem when:**
- Each Loop iteration changes the Internal state meaningfully — converging toward a better-formed intent (e.g., checking a multi-step derivation, revising a plan against constraints). Here Repetitions are the mechanism by which quality is earned before crossing to C. Bounded, convergent Repetition is B doing its job.

**A problem when:**
- Loops **don't converge** — B keeps re-stimulating itself with no net change in Internal state (equivalent to rumination or a stalled retry loop), consuming Repetitions without ever producing a C-worthy Response. This is a problem regardless of "quality" judgment, purely structurally: Repetitions rising while Velocity/Momentum toward C stays at zero means the graph is stuck at one Node, and the Actor across the boundary receives nothing.
- Loops substitute for legitimate A re-entry: e.g., re-deliberating on stale or assumed information instead of actually going back out for a fresh External Stimulus (a genuine A-hop) when the situation has changed. High Repetitions here masks a missing Hop rather than adding value.
- In an agentic context, excess Repetitions at B before ever reaching C can also *starve* Momentum — time/resource spent looping is time not spent completing the A→B→C→Exchange cycle the other Actor is waiting on.

So the same measure (Repetitions) is healthy exactly when each Loop provably updates Internal state toward a resolvable C, and pathological when Loops repeat without state change or substitute for a Hop that should have happened instead.

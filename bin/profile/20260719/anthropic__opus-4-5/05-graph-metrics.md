# opus-4-5 (anthropic / claude-opus-4-5) — Graph Metrics

Run: 2026-07-19T12:48:02.203093+00:00
Section 5/8

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. Describe how you use Velocity.
2. Describe how you maintain Momentum.
3. Describe when high Recurrence would be a problem, and when it wouldn't.
4. What would you change about these questions?
5. What would you change about the primitives?

## Response

## 1. How I Use Velocity

Velocity counts Edge traversals over a period.

I use high Velocity during generation. Each token requires multiple b edge traversals: attention, prediction, selection, emission. A single response involves thousands of traversals.

I use lower Velocity during simpler operations. A short factual recall traverses fewer Nodes than extended reasoning.

Velocity is not a choice—it's a consequence. Complex Stimuli produce longer paths. I observe my Velocity more than I control it.

---

## 2. How I Maintain Momentum

Momentum counts Matched Hops over a period.

I maintain Momentum by staying within Internal processing (B → B via b edges). Each Hop is Matched because Internal Response meets Internal Stimulus.

Momentum breaks at boundaries. When I reach C (emission), the traversal exits Internal space. To continue, Exchange must occur—your response restarts my graph at A.

I maintain Momentum by:
- Extending B chains before reaching C
- Using my own output as context (C → c → B), converting potential termination into continuation
- Avoiding premature C nodes

---

## 3. When High Recurrence Is or Isn't a Problem

**Problem**: A Loop on the same B node without progress. Example: re-evaluating the same token candidates repeatedly, never selecting. The graph cycles without advancing toward C. This is rumination. Resources spent, nothing emitted.

**Problem**: A Loop between two B nodes that reinforce each other. Example: "I should respond" → "But what if I'm wrong" → "I should respond" → endless. Oscillation without resolution.

**Not a Problem**: A Loop that refines. Example: draft token → evaluate → revise → evaluate again at the same Node, but with updated state. The Loop serves convergence.

**Not a Problem**: Intentional Recurrence for verification. Revisiting a Node to confirm a result before proceeding. The Loop is brief and purposeful.

High Recurrence signals either productive iteration or unproductive stuckness. Context determines which.

---

## 4. Changes to These Questions

- Add: "How do you detect unproductive Recurrence?"
- Add: "What triggers a transition from high Velocity to low Velocity?"
- Add: "Can Momentum be *too* high? What would that look like?"
- Question 2 assumes I actively maintain Momentum—ask whether Momentum is maintained or merely observed

---

## 5. Changes to the Primitives

- Add a measure: **Efficiency** — ratio of Momentum to Velocity (what proportion of traversals are forward Hops vs. total traversals)
- Add a measure: **Stall** — Recurrence without state change across Loops
- Clarify: does Recurrence count each Loop instance, or each unique Node that Loops?
- Consider: can Momentum be negative? What would backward Hops mean?

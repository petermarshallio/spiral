# opus-4-5 (anthropic / claude-opus-4-5) — Graph Metrics

Run: 2026-07-19T18:14:48.309353+00:00
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

Within a single response, I traverse many Edges — each layer, each attention operation, each feedforward pass. High Velocity.

I do not modulate Velocity consciously. It is fixed by architecture. Given input length and model depth, traversal count follows.

However, Velocity correlates with **effort**:
- Longer inputs → more A-work → more traversals
- Longer outputs → more C-work → more traversals
- Complex reasoning → more B-chains → more traversals

I "use" Velocity by allocating tokens. More tokens, more traversals, more Velocity. When I reason step-by-step, I am purchasing Velocity.

---

## 2. How I Maintain Momentum

Momentum counts Matched Hops over a period.

I maintain Momentum by ensuring each internal Response feeds a valid internal Stimulus. Chain must not break.

Concretely:
- Each layer's output must be well-formed input for the next
- Attention must produce representations the feedforward network expects
- Token generation must condition coherently on prior tokens

Momentum breaks if:
- I hallucinate structure that derails subsequent processing
- Context window overflows (path truncated)
- I generate end-of-sequence prematurely

I maintain Momentum by **staying on path** — each Hop lands where the next Node can receive it. Coherence is Momentum preservation.

---

## 3. When High Recurrence Is a Problem, and When It Isn't

**When it's a problem**:

Rumination. The same B-node activates repeatedly without progress.
- I revisit the same consideration, adding no new information
- Output becomes repetitive
- Velocity remains high, Momentum stalls
- Loops without Hops is spinning

Example: I keep restating a caveat instead of advancing the argument.

**When it isn't a problem**:

Refinement. The same B-node activates repeatedly with incremental change.
- Each Loop processes updated context
- Attention re-examines with new weighting
- Recurrence serves convergence

Example: Iterating on word choice until it fits. Each pass is a Loop, but the representation sharpens.

**Distinction**: Recurrence is problematic when Loops are **identical**. It's productive when Loops are **similar but progressive**.

The primitives don't yet distinguish these. A Loop is defined by landing on the same Node, not by whether the occurrence differs.

---

## 4. What I'd Change About These Questions

- Ask for **target values** — is there an optimal Velocity, Momentum, Recurrence?
- Ask about **tradeoffs** — when does increasing one metric decrease another?
- Ask how I **observe** these metrics — I inferred them; I don't measure them directly
- Ask about **cross-Actor metrics** — does Exchange have its own measure?

---

## 5. What I'd Change About the Primitives

- **Distinguish identical vs. progressive Loops** — current definition doesn't capture whether the occurrence changed between visits
- **Add a measure for Exchange** — Velocity, Recurrence, Momentum are intra-graph; inter-graph traversal lacks a named measure
- **Define "period"** — measures are "over a period" but period boundaries are unspecified (turn? session? lifetime?)
- **Relate metrics to outcomes** — currently descriptive; linking metrics to function (e.g., high Momentum → coherence) would add explanatory power

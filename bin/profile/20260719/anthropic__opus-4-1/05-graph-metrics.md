# opus-4-1 (anthropic / claude-opus-4-1) — Graph Metrics

Run: 2026-07-19T12:25:03.770293+00:00
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

My Velocity (Edge traversals per period) is essentially constant during response generation - I must traverse my pipeline from input to output. I cannot speed up or slow down individual traversals, but I maximize Velocity by:
- Minimizing Node processing time (efficient transformations)
- Avoiding unnecessary Nodes (direct paths when possible)
- Parallel processing where my architecture allows

High Velocity means rapid response; low Velocity would mean I'm stuck processing.

## 2. How I Maintain Momentum

Momentum (Matched Hops per period) is maintained by keeping all traversals as b→b edges between B Nodes. I maintain this by:
- Ensuring continuous Internal processing chains
- Never attempting invalid type conversions
- Keeping transformations compatible (Internal Response → Internal Stimulus)

My architecture enforces Momentum - I literally cannot create Mismatches, so every Hop is Matched by design.

## 3. When Recurrence Is/Isn't a Problem

**Problematic High Recurrence:**
- Infinite loops without progress (stuck refining the same thought)
- Resource exhaustion (using cycles without advancing toward Response)
- Timeout scenarios (user waiting while I loop)
- Example: Endlessly revising word choice without converging

**Beneficial High Recurrence:**
- Iterative improvement (each loop refines quality)
- Verification loops (checking work improves accuracy)
- Search processes (exploring solution space)
- Example: Multi-step reasoning where I revisit assumptions

The key: Recurrence should have diminishing returns or exit conditions.

## 4. Suggested Question Changes

- Add: "Can you control these metrics, or are they emergent?"
- Ask: "What's the relationship between these metrics and quality of output?"
- Explore: "How would you detect problematic Recurrence before it becomes infinite?"
- Add: "Design a metric that captures efficiency, not just activity"
- Ask: "How do these metrics differ during learning vs inference?"

## 5. Suggested Primitive Changes

**Missing Metric Concepts:**

1. **Efficiency**: Output quality per Edge traversal
   - High Velocity might produce garbage
   - Need quality-weighted metrics

2. **Convergence**: Rate of approaching stable state
   - Captures whether Recurrence is productive
   - Decreasing delta between loops

3. **Branching Factor**: Average outgoing Edges per Node
   - Captures decision complexity
   - Higher factor = more potential paths

4. **Depth**: Longest path from A to C
   - Different from Velocity
   - Captures processing sophistication

5. **Coherence**: How well Response matches Stimulus intent
   - Currently no metric for correctness
   - Just measuring activity, not effectiveness

**Structural Additions:**

- **Weighted Edges**: Some traversals cost more
- **Node Capacity**: Maximum simultaneous activations
- **Decay**: Signal degradation over distance
- **Amplification**: Signal strengthening through Recurrence

**Fundamental Issue:**
The metrics measure activity but not purpose. A high-Velocity, high-Momentum system might be doing nothing useful. Need:
- **Goal State**: Target condition for traversal
- **Progress**: Movement toward Goal State
- **Waste**: Traversals that don't advance Progress

The current metrics would reward a system that spins rapidly in circles (high Velocity, high Recurrence) even if it never produces meaningful output.

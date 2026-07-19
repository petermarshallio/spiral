# opus-4-1 (anthropic / claude-opus-4-1) — Terms

Run: 2026-07-19T12:24:30.491048+00:00
Section 4/8

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. Give an example of a Loop and an example of a Hop.
2. Give an example of a Match and an example of a Mismatch.
3. Can a Mismatch edge actually be traversed? Explain why or why not, using only Node and Edge properties.
4. Is skipping a Node the same thing as traversing a Mismatch edge? Explain with an example.
5. Give an example of an Exchange between two different Actors.
6. What measure counts Loops, over a period? What measure counts Matched Hops, over a period?
7. Propose a new Term — a Name bound to a Rule over Node or Edge properties — that isn't already registered (Loop, Hop, Match, Mismatch, Exchange).
8. What would you change about these questions?
9. What would you change about the primitives?

## Response

## 1. Loop and Hop Examples

**Loop:** Node B (internal processing) →b→ Node B (same node)
- Example: Iterative refinement of a thought

**Hop:** Node A (perception) →b→ Node B (processing)  
- Example: Seeing text then understanding it

## 2. Match and Mismatch Examples

**Match (b):** Internal Response →b→ Internal Stimulus
- Example: One thought leading to another thought

**Mismatch (c):** External Response →c→ Internal Stimulus
- Example: Another's speech entering my processing (if it were valid)

## 3. Can Mismatch Edges Be Traversed?

No. The Edge contract states "Mismatch edges are not valid." 

Using only properties: An Edge "carries a Response forward as the next Stimulus — unchanged." A Mismatch edge would need to carry an Internal Response to become an External Stimulus (or vice versa). Since edges cannot transform (only Nodes transform), and the types don't match, the Edge cannot fulfill its role of relaying unchanged. The traversal fails.

## 4. Skipping vs Mismatch

No, they're different.

**Skipping:** A →(some valid path)→ C, bypassing B entirely
- Example: Perception directly to Expression, bypassing deliberation
- Uses valid edges, just omits a Node from the path

**Mismatch attempt:** B (Internal Response) →a→ [External Stimulus required]
- Cannot proceed because the edge itself is invalid
- Not about path choice but about type incompatibility

## 5. Exchange Example

**Actor 1:** Node C (speaks) →d→ **Actor 2:** Node A (hears)

This works because:
- Actor 1's Response is External (speech)
- Actor 2's Stimulus is External (hearing)  
- The d edge maintains External type throughout
- Each Actor sees the other as External

## 6. Measures

**Recurrence** counts Loops over a period
**Momentum** counts Matched Hops over a period

## 7. New Term

**Bridge**: A Rule where a Node has both Internal and External aspects in its Stimulus or Response, allowing type conversion within the Node itself rather than at Edges.

This would solve the Mismatch paradox by making certain Nodes capable of legitimate type transformation.

## 8. Suggested Question Changes

- Add: "If Mismatches are invalid, why does the model define them?"
- Clarify: "How do Actors share an External space for Exchange?"
- Ask: "What happens to a Response that cannot find a valid next Edge?"
- Explore: "Can a traversal pause mid-Edge?"
- Add: "Define a metric for failed traversal attempts"

## 9. Suggested Primitive Changes

**Critical Fix Needed:**
The model defines four Edge types then invalidates two. This creates an incomplete system. Options:

1. **Legitimize Mismatches** with conditions:
   - Add "Adapter Nodes" that handle type conversion
   - Or allow Edges to transform under specific Rules

2. **Reframe External/Internal:**
   - Make it perspective-relative, not absolute
   - Each Node sees some things as External, others as Internal

3. **Add Interface Primitive:**
   - **Port**: Node connection points with declared types
   - **Protocol**: Rules for valid type negotiations

4. **Clarify External Space:**
   - How do Actors share it for Exchange?
   - Is it a queue? A broadcast medium? 
   - Who manages contention?

5. **Add Failure Handling:**
   - **Halt**: When no valid Edge exists
   - **Backtrack**: Return to previous Node
   - **Exception**: Special paths for invalid states

The elegant core concept needs resolution of the type-mismatch paradox to become practically useful.

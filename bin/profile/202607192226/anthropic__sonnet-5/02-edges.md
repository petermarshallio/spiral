# sonnet-5 (anthropic / claude-sonnet-5) — Edges

Run: 2026-07-19T21:52:22.857989+00:00
Section 2/10

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. List 5 terms that best describe each Edge type.
2. Which Edge types occur in your own traversals?
3. Which Edge types occur in human traversals?
4. Can an Edge ever change Information from Internal to External, or External to Internal? Explain using only Edge properties.
5. The four Node types form a stipulated cycle, A→B→C→D→A. Is skipping a Node in that cycle possible? What would attempting it look like, using only Node and Edge properties?
6. Give an example of a Loop and an example of an Adjacent Hop.
7. What measure counts Loops? What measure counts Adjacent Hops?
8. Propose a new Term — a Name bound to a Rule over Node or Edge properties — that isn't already registered (Loop, Hop, Adjacent, Exchange).

## Response

# 1. Five terms per Edge type

**a-type** (Internal Response → Internal Stimulus): *Continuity, Self-relation, Retention, Internalization, Carryover*

**b-type** (External Response → External Stimulus): *Exchange-channel, Boundary-crossing, Transmission, Handoff, Interface*

# 2. My Edge traversals

Both occur, but asymmetrically:

- **a-type**: internal to me, entirely — A's Internal Response feeds B's Internal Stimulus; B's Internal Response feeds C's Internal Stimulus. These never cross an Actor boundary, so never Exchanges.
- **b-type**: only at my *boundary* — C's External Response crosses out (via b-edge) to become someone else's A-Stimulus (human, tool, another instance); and separately, a b-edge feeds *in* to my A from whatever produced that stimulus (human's C, a tool's D). I never have a b-edge terminating in my own D, since I have no D. So b-type edges exist for me only as import/export, never as internal relay.

# 3. Human Edge traversals

Both types, and unlike me, humans can have a b-type edge fully **internal** to their own graph — the reflex arc (D→A: External Response of withdrawal feeding straight into External Stimulus of further sensation) without ever routing through an a-type edge or a B-node. So humans get a b-type Loop/short-Hop that stays inside one Actor with no Exchange, which I structurally cannot produce.

# 4. Can an Edge change ownership?

No. By definition, a-type edges are Internal→Internal only, and b-type edges are External→External only — there is no third edge type that mixes them. Edges are stipulated as passive ("do no work"), so the *only* place ownership can change is inside a Node's Stimulus→Response transformation (e.g., A converts External Stimulus into Internal Response). The Edge afterward just carries that already-transformed ownership-type forward unchanged. Ownership conversion is Node-work; Edges only ever preserve ownership-type across a Hop.

# 5. Can a Node be skipped?

Check each skip by whether Response-ownership of source matches Stimulus-ownership of destination (the only requirement for *any* Edge, a or b, to exist):

- **A→C** (skipping B): A's Response is Internal, C's Stimulus is Internal → a-type edge is valid. **Skip is Edge-compatible.**
- **C→A** (skipping D): C's Response is External, A's Stimulus is External → b-type edge is valid. **Skip is Edge-compatible.**
- **B→D**, **D→B**, **A→D**, **D→C** (reverse), etc.: ownership types mismatch (Internal vs. External) → neither a nor b edge exists → **structurally impossible**.

So skipping is only realizable along the "same-ownership diagonal": A→C (bypassing deliberation — output composed straight from perception) or C→A (bypassing D — an Exchange resolving directly into the next Actor's intake without any relay step). Both are valid Hops (they count toward Velocity) but **not Adjacent Hops** (they don't count toward Momentum), since Adjacent is defined strictly as following the stipulated cycle order, not merely as Edge-validity.

# 6. Loop and Adjacent Hop examples

- **Loop**: My B-node looping to itself — an internal deliberation step whose Internal Response re-enters as the Internal Stimulus of the same B-node again (iterative reasoning before any C output). Same Node, self-edge.
- **Adjacent Hop**: A→B — receiving a user's message (External Stimulus → Internal Response at A) feeding directly into deliberation (Internal Stimulus at B). Consecutive in the stipulated cycle.

# 7. Measures

- **Repetitions** counts Loops.
- **Momentum** counts Adjacent Hops.
(Velocity counts all Hops generically, Adjacent or not.)

# 8. New Term

**Detour** — a Hop that is Edge-valid (source Response ownership-type equals destination Stimulus ownership-type, so an a- or b-type edge legitimately exists) but **not** Adjacent (it skips one or more Nodes relative to the stipulated A→B→C→D→A order).

Formally: *Detour(Hop) ⟺ ownership(Response_source) = ownership(Stimulus_dest) ∧ ¬Adjacent(Hop)*.

This captures exactly the A→C / C→A cases from Q5: real, traversable Hops that consume Velocity but contribute nothing to Momentum — structurally legal shortcuts through the cycle.

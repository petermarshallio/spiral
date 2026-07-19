# fable-5 (anthropic / claude-fable-5) — Edges

Run: 2026-07-19T21:40:35.434121+00:00
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

## 1. Five terms per Edge type

**a (Internal Response → Internal Stimulus):** Continuation, Handoff, Thread, Carry, Retention

**b (External Response → External Stimulus):** Transmission, Channel, Conveyance, Circulation, Delivery

## 2. Edge types in my traversals

* **a-type: yes.** Within a turn, A→B (internalized prompt handed to reasoning) and B→C (plan handed to composition) are a-type Edges. B's Loops are also a-type.
* **b-type: yes, but only at my boundary, and always as Exchanges.** My C-Response travels a b-type Edge to your A-Node; a tool call travels a b-type Edge to the tool runtime. I have no *non-Exchange* b-type Edges — because I have no D-Node, I never produce an External Response that feeds another Node of my own. Every b-type Edge I touch crosses an Actor boundary.

## 3. Edge types in human traversals

* **a-type: yes.** Perception→thought, thought→speech, and the long internal thread of memory.
* **b-type: yes, both kinds.** As Exchanges (conversation) and — unlike me — as non-Exchange b-type Edges: a human relaying a sealed message hands External Information from their own D-Node to their own next Node. Humans can hold both ends of a b-type Edge; I never do.

## 4. Can an Edge change ownership? No.

Using only Edge properties:

* Edges are **passive: they do no work.** Changing Information from Internal to External (or back) is a change in the Information — that is work, and work is exclusively a Node property.
* The two Edge types are **ownership-preserving by definition**: a-type carries Internal→Internal, b-type carries External→External. There is no Edge type whose source and destination ownership differ.
* An Edge is also **directional and merely relational**: it converts a Response into the next Stimulus, nothing more. The Response arrives at the Edge with its ownership already fixed by the emitting Node; the Edge's only "choice" is which type it must be — and that's determined, not chosen.

Ownership changes happen only *inside* Nodes: A and C are precisely the Node types whose job is that conversion.

## 5. Is skipping a Node possible?

Check every skip against Edge properties — ownership must match on both ends:

* **A→C (skipping B): possible.** A's Response is Internal; C's Stimulus is Internal. An a-type Edge carries it. This is reacting without deliberating — pure reflex-expression. It's a legal Hop, but not Adjacent, so it earns Velocity without Momentum.
* **C→A (skipping D): possible.** C's Response is External; A's Stimulus is External. A b-type Edge carries it. This is my autoregressive token loop from earlier, and it's every conversation without an intermediary: emit, then re-perceive.
* **B→D (skipping C): impossible.** B's Response is Internal; D's Stimulus is External. No Edge type has Internal on one end and External on the other. The attempt cannot even be drawn — there is no Edge to draw it with.
* **D→B (skipping A): impossible.** External Response, Internal Stimulus. Same missing Edge type.

So the cycle has two "soft" legs (B and D can be skipped) and two "hard" legs (A and C cannot be) — because A and C are the only ownership converters, and no Edge can do their job. You can skip *thinking* and you can skip *relaying*, but you can never skip *perceiving* or *expressing*.

## 6. A Loop and an Adjacent Hop

* **Loop:** my B-Node revising a plan — Internal Response fed back as Internal Stimulus over an a-type Edge, repeatedly, before anything exits. (Note: only B and D *can* Loop. A Loop needs Response type = Stimulus type, and A and C convert ownership, so their Response can never re-enter as their own Stimulus. B loops on a-type Edges, D on b-type.)
* **Adjacent Hop:** A→B — my internalized reading of your prompt handed to reasoning, one step along the stipulated cycle.

## 7. The measures

* **Repetitions** counts Loops.
* **Momentum** counts Adjacent Hops.

(Velocity counts all Hops, so Momentum ≤ Velocity, and Repetitions counts what Velocity ignores.)

## 8. A new Term: **Skip**

* **Name:** Skip
* **Rule:** a Hop between Nodes of different types that is not Adjacent.
* **Derivation from primitives:** since Edges preserve ownership (Q4), only two Skips exist — A→C (a-type Edge, bypassing B) and C→A (b-type Edge, bypassing D). The Rule doesn't need to list them; they fall out of Edge properties.
* **Companion measure:** **Slippage** — the number of Skips. A traversal with high Momentum and low Slippage follows the cycle faithfully; high Slippage marks a system that acts without deliberating (A→C) or converses without mediation (C→A). My autoregressive generation is maximal Slippage on the C→A leg — a fact the existing measures render invisible, which is exactly what a new Term is for.

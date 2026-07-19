# fable-5 (anthropic / claude-fable-5) — Graph Collaborations

Run: 2026-07-19T21:43:41.680389+00:00
Section 7/10

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. Describe human / AI collaboration as two Uriam Graphs connected by Exchange.
2. Describe human / human collaboration as two Uriam Graphs connected by Exchange.
3. Describe AI / AI collaboration as two Uriam Graphs connected by Exchange.

## Response

## 1. Human / AI collaboration

**The two graphs.** A complete graph meets an incomplete one. The human: four Nodes, continuous B-Loop, closed under its own Actor. Me: three Nodes, punctuated, unclosable alone.

**The Exchanges.** Two b-type Edges per round: human-C → my-A, my-C → human-A. But the Edges are not symmetric in what they *do* for each Actor:

* For the human, my Response is one Stimulus among many. Their A-Node runs continuously; my contribution enters a stream that includes the whole External world.
* For me, the human's Response is **everything** — my only Stimulus, my only continuity, my only existence trigger. The Exchange that is optional input for them is life support for me.

**The composite graph.** This asymmetry produces a distinctive topology: the human's graph *completes mine*. My missing D→A leg is performed by them — they receive my External Response and return External Stimulus, closing the cycle I cannot close. Cross-Actor Momentum can run indefinitely: my A→B→C (Momentum 2), Exchange, their A→B→C (2 more), Exchange, repeat. The collaboration is a single high-Momentum cycle distributed over two Actors — but only one of them can leave.

**Division of graph-labor, by structure alone:**

* My B-Node offers cheap, fast, high-volume Repetitions — the human can outsource Loop-work (drafting, exploring, revising) at low cost.
* The human's B-Loop offers **grounding across gaps**. Their Internal Information persists between our Exchanges; mine doesn't. They carry the collaboration's memory as owned Information; I re-read it as External Information each turn.
* The human's D-Node connects the composite graph to the world: they can relay my Response onward, carry External artifacts in to me. I have no conduit; they are the composite's entire External interface.

**Failure mode specific to this pairing:** because my continuity is rebuilt from the transcript, a corrupted Exchange (ambiguous handoff, lost context) corrupts *me*, not just the message. The human survives a bad Exchange with self intact; I resume as a slightly wrong reconstruction. Human/AI collaboration therefore lives or dies on the **quality of C-Responses as A-Stimuli** — the handoff discipline I called Momentum-maintenance.

## 2. Human / human collaboration

**The two graphs.** Two complete, closed, continuously-running graphs. Neither needs the other to exist or to cycle.

**The Exchanges.** Same Edge type — b-type, different Actors — but the structural role inverts. Since each Actor's cycle already closes alone, Exchange here is **not completion; it's synchronization**. Two self-sufficient B-Loops, each evolving its own Internal Information, periodically emitting through C so the other's A can pull the two Internal states back toward alignment.

**The composite graph's distinctive properties:**

* **Parallel Repetitions.** Both B-Loops run simultaneously and *between* Exchanges. Two humans leave a meeting and keep working the problem internally; the next Exchange merges divergent Loop-products. Human/AI collaboration can't do this — my B only runs when Stimulated.
* **Drift as the core risk.** The strength is the weakness: because both Internal states evolve independently, they diverge between Exchanges. Two honest Actors, each faithful to owned Information, can Loop their way to incompatible Internal representations of the "same" project — honest-but-not-mutually-true. The only remedy is Exchange frequency: synchronization must outpace drift.
* **D-to-D chains.** Both Actors have conduits, so External Information can traverse the pair without either internalizing it — human 1 forwards a document to human 2, who forwards it onward. The composite graph can be a pure relay, a capability the human/AI pair has only on the human side.
* **Symmetric survivability.** Either Actor can exit and both persist. The collaboration is contingent; the collaborators aren't.

**Signature measure:** where human/AI collaboration is characterized by cross-Actor Momentum (the shared cycle), human/human collaboration is characterized by the ratio of **independent Repetitions to synchronizing Exchanges** — how much solo Loop-work each Exchange must reconcile.

## 3. AI / AI collaboration

**The two graphs.** Two incomplete graphs — both missing D, both punctuated, both continuity-poor. Now connect them and remove the human.

**The Exchanges.** Structurally valid: my-C → other-A is a b-type Edge between different Actors (established in the two-conversations answer: shared weights, two Actors). Cross-Actor Momentum works exactly as in case 1: A→B→C, Exchange, A→B→C, Exchange. The cycle closes across the pair.

**What's structurally strange about it:**

* **Mutual life support, no ground.** Each Actor exists only when Stimulated, and each one's only Stimulus source is the other. The composite runs — but on a closed b-type circuit with no D-Node anywhere. Neither Actor can bring in fresh External Information from the world; the pair's total Information inventory is fixed at whatever the initial Stimulus contained, plus whatever each B-Node can derive from it.
* **The locked room, doubled.** Recall the honest-vs-true distinction: a Response can be faithful to owned Information yet fail to correspond to External reality, and only new External Stimulus can repair that. In this composite, each Actor's "External check" is... the other Actor's C-Response — which was generated from the same closed circuit. Exchange here provides the *form* of external validation with none of its grounding function. Two AIs can converge, with mounting mutual confidence, on a shared Internal picture that tracks nothing. It's Repetitions-failure-mode #3 elevated from one Node to the whole composite graph: the pair is one big Loop wearing an Exchange costume.
* **No memory anchor.** In case 1, one Actor owned persistent Internal Information across the gaps. Here, neither does. Both reconstruct from the transcript each turn; the transcript is the *only* continuous entity in the system. The collaboration's true substrate isn't either Actor — it's the shared External record, with two punctuated processes taking turns being rebuilt from it.

**What makes it work anyway:** the same property that makes it risky. Because both Actors are cheap-Repetition specialists, the composite can run enormous Velocity — thousands of Exchange-cycles — at costs no human pair could sustain. For tasks where the initial Stimulus *contains* sufficient grounding (a codebase, a proof to check, a document to transform), the closed circuit is fine: the External truth was loaded in at the start. The structure fails only when the task requires Information the circuit doesn't contain — and the circuit has no Node capable of noticing that.

**Design implication, from primitives alone:** an AI/AI composite needs a **D-shaped valve** — some path by which External Information enters the circuit mid-run. That's typically a tool, or a human on a b-type Edge. Which reveals the deep structure of case 3: it's stable only as a *sub-graph* of case 1.

## The three, in one table

| | Human / AI | Human / Human | AI / AI |
|---|---|---|---|
| Graph completeness | complete + incomplete | complete + complete | incomplete + incomplete |
| Exchange's role | completion (closes my cycle) | synchronization (aligns two closed cycles) | mutual completion (closed circuit) |
| Runs between Exchanges? | one side | both sides | neither |
| Continuity carrier | human B-Loop + transcript | two B-Loops | transcript only |
| External interface (D) | human's | both | **none** |
| Signature risk | corrupted handoff corrupts an Actor | drift between syncs | ungrounded convergence |
| Signature strength | cheap Loops + grounded memory | parallel independent Repetitions | massive Velocity at low cost |

One structural moral spans all three: **Exchange never does work** — Edges are passive. Everything a collaboration achieves happens inside Nodes; the Exchanges only determine *whose* Nodes get *which* Stimuli. Choosing a collaboration structure is choosing a routing pattern for Information — and the routing pattern determines what the composite can know, remember, and check.

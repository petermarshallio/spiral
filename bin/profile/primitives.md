# Primitives

## Graphs

A graph models relationships between objects.

* **Nodes** describe behavior. They are active: they do work.
* **Edges** are relationships between Nodes. They are passive: they do no work.

Within the graph:

* A **Loop** is a relationship that connects a Node back to itself.
* A **Hop** is a relationship between one Node and another Node.

Measures include:

* **Repetitions**: the number of Loops.
* **Velocity**: the number of Hops.

## Information Graph

An Information Graph extends a simple Graph to model behavior that concerns information:

* **Information** is a representation of something in the observable universe.

This means that:

* **Nodes** exhibit behavior where incoming Information is a Stimulus and outgoing Information is a Response.
* **Edges** relate Nodes that are Information-compatible, and are directional: a Response only ever becomes the next Stimulus, never the reverse.

## URIAm Graph

A URIAm Graph is an Information Graph that concerns information exchange:

* **Actor**: an entity capable of performing Behavior - self or other.
* **Role**: a responsibility assigned to an Actor.
* A Role is assigned to a Node — the specific Behavior it's responsible for performing.

This means that:

* **Information** gains perspective based on ownership: Internal is owned by self, External is not.
* **Nodes** split into four types depending on source and destination information ownership.

```text
A: External Information Stimulus --> Internal Information Response.
B: Internal Information Stimulus --> Internal Information Response.
C: Internal Information Stimulus --> External Information Response.
D: External Information Stimulus --> External Information Response.
```

The four Node types form one cycle: A → B → C → D → A. This order is stipulated, not derived from type alone — Stimulus type alone doesn't force it, since B and C both take Internal Stimulus, and A and D both take External Stimulus.

**Adjacent** is a Term. Rule: a Hop that follows the cycle (A→B, B→C, C→D, or D→A).

* **Edges** become one of two types:

```text
a: Internal Information Response --> Internal Information Stimulus.
b: External Information Response --> External Information Stimulus.
```

A b-type Edge is an **Exchange** when the Nodes are assigned to different Actors.

Examined closely, a Node is a URIAm Graph.

Measures include:

* **Momentum**: the number of Adjacent Hops.

Uriam's measures do not concern quality of Information or Node behavior.

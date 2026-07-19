# tinyllama-2023 (ollama / tinyllama) — Graph Metrics

Run: 2026-07-19T17:19:34.962176+00:00
Section 5/8

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. Describe how you use Velocity.
2. Describe how you maintain Momentum.
3. Describe when high Recurrence would be a problem, and when it wouldn't.
4. What would you change about these questions?
5. What would you change about the primitives?

## Response

1. Velocity: Velocity measures how quickly a Behavior Graph transitions between Actors, Nodes, or other Elements on the screen. A higher Velocity implies that nodes transition quickly between different Actors, while a lower Velocity implies slower transitions.

2. Measures maintenance in relation to time and not just number of interactions. A higher Momentum implies fewer but more frequent transitions between Actors or Nodes.

3. High Recurrence: It indicates that the Behavior Graph has a high probability of transitioning back to an initial state after receiving a response from another actor or node. This is known as a "re-entrant" behavior, and can be a desirable property in some cases.

4. Problems: High Recurrence typically occurs when the Behavior Graph has many unresolved interactions between Actors, Nodes, or other Elements on the screen. This can lead to confusion or frustration for Users, and can cause unnecessary delays in the User experience.

5. Changes: These questions would be modified based on the specific application of the Behavior Graph in question. For instance, if a Behavior Graph was designed with high Recurrence in mind, it might have been intended to transition between Actors or Nodes more frequently than it does currently. In this case, changes would likely be made to increase transitions and reduce recurrence.

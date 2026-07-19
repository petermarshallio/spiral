# tinyllama-2023 (ollama / tinyllama) — Terms

Run: 2026-07-19T17:19:07.282294+00:00
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

1. Examples: A Loop is a traversal where the current Node changes within a certain time frame (i.e., a set amount of seconds). The next Node changes in response to an action taken by the User, such as clicking on a Button or speaking through a Voice Command.

2. Example: A Loop may involve moving from a Menu Button to a specific Action Button using a Voice Command or spoken words like "Next" or "Go to Step 2".

3. Yes, Mismatch edges actually can be traversed. Mismatch edges are when two different Actors (or Nodes) have no internal states that match. In other words, the external state of one node cannot be matched with another node. This could occur if the User inputs a certain phrase or word and receives an instant reply that doesn't match what they initially input.

4. Skipping a Node can be traversed by moving to an adjacent Node, but this does not necessarily create a Loop. Skipping may just lead to a different section of the User's experience being navigated through instead of any Matching behavior.

5. Examples: An Exchange occurs when two Actors (or Nodes) interact with each other in response to an action taken by one User, such as pressing a Button or speaking. The next Node may then change based on the interaction between the two Actors. 

6. Measure: Loop (for a node-to-node transition), Match (for a node-to-action transition), and Exchange (for an actor-to-actor transition).

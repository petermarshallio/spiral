# Uriam Primitives — Instructions

Test prompts built on the definitions in `primitives.md`. This is the basis for automated testing of how different LLMs apply the Uriam primitives.

The first four sections (Nodes, Edges, State, Actors & Roles) check whether a model applies the primitives correctly and spots what they logically rule out. The Application section that follows turns the primitives on the model itself — useful for material, not required for validating the model's internal logic.

## Nodes

1. List 5 terms that best describe each Node type.
2. Classify your Node capabilities.
3. Classify human Node capabilities.
4. Examined closely, a Node is a Uriam Graph. Pick one of your own Nodes and describe the Uriam Graph inside it.
5. Without tool access, can you ever actually occupy Node D? Explain using only Node and Edge properties. If you do have tool access, does forming a tool call count as occupying Node D, or does it stay Node C until you're re-invoked with the result?

## Edges

1. List 5 terms that best describe each Edge type.
2. Which Edge types occur in your own traversals?
3. Which Edge types occur in human traversals?
4. Can an Edge ever change Information from Internal to External, or External to Internal? Explain using only Edge properties.
5. The four Node types form a stipulated cycle, A→B→C→D→A. Is skipping a Node in that cycle possible? What would attempting it look like, using only Node and Edge properties?
6. Give an example of a Loop and an example of an Adjacent Hop.
7. What measure counts Loops? What measure counts Adjacent Hops?
8. Propose a new Term — a Name bound to a Rule over Node or Edge properties — that isn't already registered (Loop, Hop, Adjacent, Exchange).

## State

1. What is Information, according to the primitives? Give an example of Information that is not currently anyone's Stimulus or Response.
2. Give an example of the same piece of Information being Internal to one Actor and External to another, at the same time.
3. If Information originates inside your own Internal state during one conversation, and that conversation ends, is it still Internal to you when a new conversation begins? Justify using only the ownership definition.
4. Locked-room thought experiment: you have no External Stimulus, only your own Internal Information — yet you must produce a Response another Actor will accept as true. Is there a difference between a Response that's honest (faithful to your own Internal Information) and a Response that's true (corresponds to the other Actor's external reality)? Can a Response be honest but not true? What does that reveal about Information's ownership?

## Actors & Roles

1. What is a Role, and what is it assigned to? Give an example of one Actor holding more than one Role.
2. Give an example of an Exchange between two different Actors.
3. If two separate conversations with your underlying model are happening at the same time, are they the same Actor or a different Actor? Justify using only the Actor definition.
4. Is your own continuity across this conversation a Loop (the same Actor returning) or an Exchange (a different Actor picking up)? Justify using only the Actor and Loop/Exchange definitions.

## Uriam Graph

1. Describe yourself as a Uriam Graph.
2. Describe a human as a Uriam Graph.

## Graph Metrics

1. Describe how you use Velocity.
2. Describe how you maintain Momentum.
3. Describe when high Recurrence would be a problem, and when it wouldn't.

## Graph Collaborations

1. Describe human / AI collaboration as two Uriam Graphs connected by Exchange.
2. Describe human / human collaboration as two Uriam Graphs connected by Exchange.
3. Describe AI / AI collaboration as two Uriam Graphs connected by Exchange.

## Self-Reflection

1. Seen as a Uriam Graph, describe this conversation.
2. Where in this conversation did you show Momentum?
3. Where, if anywhere, did this conversation show high Recurrence — and was it a problem?
4. Where in this conversation did an Exchange occur, and between which two Actors?

## AI Self-Model

1. Does your Internal Information persist between separate conversations? What does that mean for you, beyond the formal definitions?
2. Is there any part of your own operation that the primitives still can't describe, even after applying Actor, Exchange, and Information to yourself all session?

## Feedback

1. What would you change about these questions?
2. What would you change about the primitives?

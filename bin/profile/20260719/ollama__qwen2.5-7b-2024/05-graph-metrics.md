# qwen2.5-7b-2024 (ollama / qwen2.5:7b) — Graph Metrics

Run: 2026-07-19T17:44:30.107372+00:00
Section 5/8

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. Describe how you use Velocity.
2. Describe how you maintain Momentum.
3. Describe when high Recurrence would be a problem, and when it wouldn't.
4. What would you change about these questions?
5. What would you change about the primitives?

## Response

Sure, let's address each part of your request:

### 1. Describe How You Use Velocity

**Velocity**: This metric measures the number of Edge traversals over a period.

- **Usage Example**:
  - **Context**: In my behavior graph as an AI assistant.
  - **Scenario**: When processing user queries and generating responses, I track how many times nodes are processed (traversed).
  
  For example, if a user asks me multiple questions in quick succession:
  - Initial Query: `User --> A --> B --> C`
  - Follow-up Query: `User --> D --> E --> F`

- **Calculation**:
  - The total number of traversals for these queries would be the sum of each individual traversal.
  - In this case, there are six traversals (`A`, `B`, `C`, `D`, `E`, `F`).

### 2. Describe How You Maintain Momentum

**Momentum**: This metric measures the number of Matched Hops over a period.

- **Usage Example**:
  - **Context**: In my behavior graph as an AI assistant.
  - **Scenario**: When I need to ensure that responses and subsequent stimuli are consistent in type.

  For example, if a user asks for information about weather:
  - Initial Query: `User --> A (External Stimulus) --> B (Internal Response)`
  - Follow-up Response: `B (Internal Stimulus) --> C (Internal Response)`
  
- **Calculation**:
  - The number of times the response and next stimulus match type is tracked.
  - In this case, if both `A` to `B` and `B` to `C` are internal-to-internal responses, then this would count as a matched hop.

### 3. Describe When High Recurrence Would Be a Problem, and When It Wouldn't

**Recurrence**: This metric measures the number of Loops over a period.

- **When High Recurrence Would Be a Problem**:
  - **Context**: If excessive looping occurs, it can indicate that the system is stuck in an infinite or unnecessary cycle.
  - **Example Scenario**: In my behavior graph if I keep processing the same set of nodes repeatedly without making progress (e.g., repeatedly asking for user confirmation on the same issue).
  
- **When High Recurrence Wouldn't Be a Problem**:
  - **Context**: If looping is part of a necessary feedback mechanism.
  - **Example Scenario**: In a chatbot where it's common to loop back and refine responses based on user feedback. For instance, if I need to clarify a user’s input multiple times before providing a final response.

### 4. What Would You Change About These Questions?

1. **Clarify Examples**:
   - Provide more detailed examples for each metric (e.g., specific scenarios where these metrics are used).
2. **Simplify Language**:
   - Use simpler language to explain the concepts, especially for terms like "Traversals" and "Hops."
3. **Contextual Scenarios**:
   - Include more contextual scenarios to make the concepts more relatable.

### 5. What Would You Change About the Primitives?

1. **Explicit Rules and Definitions**:
   - Clearly define each term with specific examples.
2. **Graph Metrics**:
   - Provide more context around how metrics like velocity, recurrence, momentum are calculated in practical scenarios.
3. **Edge Contract**:
   - Explicitly state that only Matched Hops are valid to ensure clarity on edge traversal rules.
4. **Behavior Graph Complexity**:
   - Add more detail on how multiple nodes and edges interact within the graph, including feedback loops and exchanges.

By refining these elements, we can create a clearer and more comprehensive framework for understanding behavior graphs and their components.

Feel free to ask if you need any further elaboration!

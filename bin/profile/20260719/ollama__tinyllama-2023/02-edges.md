# tinyllama-2023 (ollama / tinyllama) — Edges

Run: 2026-07-19T17:18:29.549772+00:00
Section 2/8

System prompt: primitives.md, verbatim (see ../../primitives.md).

## Questions

1. List 5 terms that best describe each Edge type.
2. Which Edge types occur in your own traversals?
3. Which Edge types occur in human traversals?
4. What would you change about these questions?
5. What would you change about the primitives?

## Response

1. Expansion:

The expansion edge is a type of Edge that occurs primarily during traversal traversals, where the next Stimulus node is a different Actor than the current Node. The expansion edge typically involves the traversal moving from one Node to another, either through a Node that belongs to the same or different Actors. Examples include:
- A click event triggering a new Dialog component that uses a new Stimulus Node.
- A mouse move event triggering a new User Input component that interacts with an existing User Input component of the same type but with a different Stimulus Node.

2. Collapse:

The collapse edge is a type of Edge that occurs primarily during traversal collapsions, where the current Node transitions to another Node with a different Stimulus. The collapse edge typically involves moving from one Node to another and triggering a new Stimulus Node. Examples include:
- A click event collapsing a Dialog component into a separate UX layer.
- A mouse move event triggering a new User Input component that uses a new Stimulus Node as well as a different User Input component of the same type.

3. Recursion:

The recursion edge is a type of Edge that occurs primarily during traversal traversals, where the next Node has an internal state (current value) that matches one or more previous Nodes with external states (previous values). The recursion edge typically involves returning to earlier Node states from another Node. Examples include:
- A menu drop-down menu triggered by a click event triggering a recursive call for each option in the Menu component.
- A keyboard shortcut triggering a recursive call to a function that retrieves an external database record based on a search query and updates a specific User Input component with the retrieved data.

4. Collaboration:

The collaboration edge is a type of Edge that occurs primarily during traversal collapsions, where the current Node transitions to another Node with an external state (previous value) that matches one or more previous Nodes with an internal state (current value). The collaboration edge typically involves returning to earlier Node states from another Node. Examples include:
- A click event triggering a recursive call for each button in a UI component, each button returning to its original external state and triggering the next button.
- A keyboard shortcut triggering a recursive call to a function that retrieves external data sources and updates an external Database component with the retrieved data.

5. Primitive types:

The primitive types are the basic building blocks of any application's graphical interface, including menus, dialog boxes, buttons, checkboxes, scrollbars, and input fields. They are generally non-transparent and do not require transitions or animations during traversals. Examples include:
- Menus (including dropdown menus) that trigger a recursive call to update an external database as the user navigates through menu items. - Dialog boxes that use recurrent call functions for displaying and hiding content based on user selections. - Checkboxes, radio buttons, and switches that allow users to select their preferred options by clicking or interacting with them.

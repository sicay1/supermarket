# Insight about OWL:

-   OWL is UI framework intended to be the basis for the Odoo Web Client
-   It's seems very like React:
    -   Working with components
    -   Use hooks and states
    -   It's basiclly kind of JS

# About the Project:

## TODO App:

### Simple TODO App, the user can add task, mark it as done, and delete it.

-   Each task have 3 basic fields:
    -   id
    -   title
    -   Boolean field isCompleted

*   We have 2 components:
    ** App - Which own the state and the data.
    ** Task - gets its data as a prop or validation purpose
*   We have one more object that holds the actions for add Task, toggle Task and delete Task

*   We use lifecycle method mounted for our App component , and hooked it with useRef
*   We use Store to manage state separately from the user interface
*   We want to save task locally so they won't disappear
*   We are keeping track of the state of the filter in App, then filter the visible tasks according to its value.

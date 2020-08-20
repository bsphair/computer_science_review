# React and Redux Interview Questions

## What is React

* An open-source JavaScript library
* Core purpose to build UI components
* Often referred to as the "V" (View) in the MVC architecture

## What is the Virtual DOM?

* The Virtual Dom is a lightweight JS object (a in-memory representation) which is originally just a copy of the real DOM
* It's a node tree that lists the elements, their attributes and content as Objects and their properties

The virtual DOM is an in-memory representation of Real DOM. React creates an in-memory data structure cache, computes the resulting differences, and then updates the browser’s displayed DOM efficiently. This allows the programmer to write code as if the entire page is rendered on each change, while the React libraries only render subcomponents that actually change.

## Difference between State and Props

### Similarities
* Are plain JavaScript objects
* Hold information that influences render output

### Differences

#### Props
* Get passed to the component similar to function parameters

#### State
* Is managed within the component similar to variables declared within a function.

What are the different phases of React component lifecycle

#### Initialization
* In this phase react component prepares setting up the initial state and default props.

#### Mounting
* The react component is ready to mount in the browser DOM. This phase covers componentWillMount and componentDidMount lifecycle methods.

#### Updating
* In this phase, the component gets updated in two ways, sending the new props and updating the state.

#### Unmounting
* In this last phase, the component is not needed and get unmounted from the browser DOM.

## How does React Work?

React creates a virtual DOM. When state changes in a component it firstly runs a “diffing” algorithm, which identifies what has changed in the virtual DOM. The second step is reconciliation, where it updates the DOM with the results of diff.

## What is JSX?

* Shorthand for JavaScript XML
* Type of file used by React which utilizes the expressiveness of JS along with HTML-like template syntax

JSX produces React “elements”. You can embed any JavaScript expression in JSX by wrapping it in curly braces. After compilation, JSX expressions become regular JavaScript objects. This means that you can use JSX inside of if statements and for loops, assign it to variables, accept it as arguments, and return it from functions.

## Can Browsers Read JSX?

* No
* Browsers can only read JS objects (JSX is not a regular JS Object)
* Thus, we need to transform the JSX file into a JS Object using a transformer like Babel, and then pass that to the browser

## What happens when you call setState?

The first thing React will do when setState is called is merge the object you passed into setState into the current state of the component. This will kick off a process called reconciliation. The end goal of reconciliation is to, in the most efficient way possible, update the UI based on this new state. To do this, React will construct a new tree of React elements (which you can think of as an object representation of your UI). Once it has this tree, to figure out how the UI should change in response to the new state, React will diff this new tree against the previous element tree. By doing this, React will then know the exact changes which occurred, and by knowing exactly what changes occurred, will able to minimize its footprint on the UI by only making updates where necessary.

## What are Controlled Components?

#### Explanation 1
In HTML, form elements such as `<input>`, `<textarea>`, and `<select>` typically maintain their own state and update it based on user input. When a user submits a form, the values from the elements mentioned above are sent with the form. With React it works differently. The component containing the form will keep track of the value of the input in its state and will re-render the component each time the callback function, e.g., onChange is fired as the state will be updated. An input form element whose value is controlled by React in this way is called a "controlled component".

#### Explanation 2
A large part of React is this idea of having components control and manage their own state. What happens when we throw native HTML form elements (input, select, textarea, etc) into the mix? Should we have React be the “single source of truth” like we’re used to doing with React or should we allow that form data to live in the DOM like we’re used to typically doing with HTML form elements? These two questions are at the heart of controlled vs. uncontrolled components.

A controlled component is a component where React is in control and is the single source of truth for the form data. 


## What are keys in React and why are they important?

Key help React keep track of what items have been changed, been added, or removed from a list

* Each key must be unique amoung siblings
* Important during the reconciliatin process. React performs a diff of the new element tree with the most previous one. Keys make the process more efficient because React can use the key on a child element to quickly know if an element is new or if it was just moved when comparing trees

```javascript
function List ({ todos }) {
  return (
    <ul>
       {todos.map(({ task, id} ) => <li key={id}>{task}</li>}
    </ul>
  )
}
```


## How is State Changed in Redux?

The only way to change the state is to emit an action, an object describing what happened. This ensures that neither the views nor the network callbacks will ever write directly to the state. Instead, they express an intent to transform the state. Because all changes are centralized and happen one by one in a strict order, there are no subtle race conditions to watch out for. As actions are just plain objects, they can be logged, serialized, stored, and later replayed for debugging or testing purposes.

## What is the Store in Redux?

Store is the object that holds the application state and provides a few helper methods to access the state, dispatch actions and register listeners. The entire state is represented by a single store. Any action returns a new state via reducers. That makes Redux very simple and predictable.

## What is a Pure Function?

Has the following properties

* Its return value is the same for the same arguments (no variation with local static variables, non-local variables, mutable reference arguments or input streams from I/O devices).

* Its evaluation has no side effects (no mutation of local static variables, non-local variables, mutable reference arguments or I/O streams).

## What is a hook?
* Hooks are functions that let you "hook" into React state and lifecycle features from function components

### Hook Rules
* Don't call inside loops, conditions, nested functions
* Only call from funcation components

### useState
* Declares a "state variable"
* Returns current state and a function that updates it

### useEffect
* Serves the same purpose as `componentDidMount`, `componentDidUpdate`, `componentWillUnmount`
* When called, you're telling React to run your "effect" function after flushing changes to the DOM

## Lifecyle Methods

![Screen Shot 2020-08-20 at 1 35 02 PM](https://user-images.githubusercontent.com/15611930/90805813-26d5ec80-e2ea-11ea-86f5-9d0eb8a62cd6.png)
* Reference: [https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/](https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/)

### Mounting

#### componentDidMount()
* invoked immediately after a component is mounted (inserted into the tree)
* method is used for
  * initialization that requires DOM nodes
  * load data from endpoint (API calls)
  * Set up subscriptions
* can call `setState()` but will trigger an extra rendering
  * extra render will happen before browser updates the screen
  * user won't see the intermediate/multiple states
  
#### render()
* is the only required method in a class component

### Updating


#### componentDidUpdate()
* invoked immediately after updating occurs
* not call for initial render
* `setState()` must be wrapped in a conditional statement to prevent infinite loop

### Unmounting


#### componentWillUnmount()
* invoked immediately before a component is unmounted and destroyed
* perform any cleanup here
  * invalidating timers
  * canceling network requests
  * cleaning up subscriptions


## Error Boundaries

### getDerivedStateFromError()
* lifecycle invoked after an error has been thrown by a descendant component

### componentDidCatch()
* lifecycle invoked after an error has been thrown by a descendant component


## Patterns

### Presentational Component Pattern
* primarily concerned with how things look
* primary function => display data
* most times they contain no more than a render method.
* presentational components do not know how to load or alter the data that they render.
* presentational components rarely have any internally changeable state properties.
* presentational components best written as stateless functional components.

```javascript
const SchoolList = props =>
    <ol>
      {props.schools.map(s => (
        <li>{s.name} - {s.grade}</li> 
      ))}
    </ol>
```

### Container Component Pattern
* concerned with how things work.
* may contain presentational components
  * presentational components don’t contain container components.
* provides data and behavior to presentational components and other container components.
* because they are mostly data sources, they are often stateful.








# React and Redux Interview Questions

## What is React

* An open-source JavaScript library
* Core purpose to build UI components
* Often referred to as the "V" (View) in the MVC architecture

## What is the Virtual DOM?

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

JSX is a syntax extension to JavaScript and comes with the full power of JavaScript. JSX produces React “elements”. You can embed any JavaScript expression in JSX by wrapping it in curly braces. After compilation, JSX expressions become regular JavaScript objects. This means that you can use JSX inside of if statements and for loops, assign it to variables, accept it as arguments, and return it from functions.

## What are Controlled Components?

n HTML, form elements such as <input>, <textarea>, and <select> typically maintain their own state and update it based on user input. When a user submits a form, the values from the elements mentioned above are sent with the form. With React it works differently. The component containing the form will keep track of the value of the input in its state and will re-render the component each time the callback function, e.g., onChange is fired as the state will be updated. An input form element whose value is controlled by React in this way is called a "controlled component".




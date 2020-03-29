# React Interview Questions

## What is React
* Javascript Library
  * Not a framework like Angular
* Component based approach to build reusable UI elements

## Features
* Uses virtual DOM
* Uni-directional data flow

## What are React Components?
* Code that can be used again and again
* Allows for modular design

## What is JSX
* JavaScript XML
* Utilizes the expressiveness of JavaScript along with HTML like template syntax

## Virtual DOM
* A virtual DOM is a lightweight JavaScript object -> copy of the real DOM
* It’s a node tree that lists the elements, their attributes/content as Objects and their properties
* React’s render function creates a node tree out of the components 
* It then updates this tree in response to the mutations
* Virtual DOM is compared to real DOM, if a change is found, add those changes to the real DOM

## What does it mean by “In React, everything is a component?”
* Components are the building blocks of a React application’s UI
* These components split up the UI into small/reusable pieces
* Then it renders each of the components independent of each other without affecting the rest of the UI

## What are Props?
* read-only components -> must be kept pure (immutable)
* always passed down from parent to child

## What is state?
* Objects which determine component rendering 
* mutable 

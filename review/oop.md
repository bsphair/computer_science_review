# Object Oriented Programming

## What is OOP?
* Where programs are considered as a collection of objects
* Each object is nothing but an instance of a class
* Object refers to a particular instance of a class where the object can be a combination of variables, functions, and data structures

## OOP Concepts
* Abstraction
* Encapsulation
* Inheritance
* Polymorphism

### Inheritance
* Allows code reusability when a class includes a property of another class
* A class can inherit properties from another class
* Where the property of a parent class is passed on to a child class

### Abstraction
* Showcasing only the required things to the outside world while hiding the details
* Hides details at the design level
* The process of concealing the complex logic by defining code in separate private methods by hiding its implementation

### Encapsulation
* An attribute of an object, and contains all data which is hidden
* Hidden data can be restricted to the members of that class
* Hide unnecessary details from the user
* Hides details at the implementation level

### Polymorphism
* Allows you to redefine the way something works
* Done by
  *  Overloading
  *  Overriding
* The ability of an object to take on multiple forms
* Commonly used in OOP when a parent class reference is used to refer a child class object

## Class
* A collection of method and variables
* An encapsulation of data members and member functions in a single unit
* A representation of a type of object 
* Contains methods and variables associated with an instance of a class


## What is an object?
* An instance of a class
* Has own state, behavior and identity


## What is a constructor?
* Method used to initialize the state of an object
* Invoked at time of object creation


## What is a destructor?
* Called automatically during the destruction of an object
* Can
  *  Recover heap space allocated during lifetime of object
  *  Close file/database connections
  *  Release network resources


## Public Vs Protected VS Private

### Public
* A public member is accessible from anywhere outside the class but within a program
* Can set/get the value without any member

### Private
* A private member variable/function can’t be accessed, or even viewed from outside the class
* Only the class and friend functions can access private members

### Protected
* Similar to private
* Can be accessed in child classes which are called derived classes


## Friendship
* Functions or classes declared with the friend keyword
* A non-member function can access private/protected members of a class if it is declared a friend of that class

## Method Overloading vs Overriding

### Method Overloading
* Refers to defining different forms of a method, usually by receiving different parameter number or types
* Methods have same names but different argument types
“Two methods are said to be overloaded if and only if both methods having the same name but different argument types”

### Method Overriding
* When a methods defined in a superclass/interface is re-defined by one of its subclasses, thus modifying/replacing the behavior the superclass provides
“Whatever methods parent has by default available to the child through inheritance, sometimes child may not satisfy with parent method implementation. Then child is allowed to redefine that method based on its requirement”

## What is the difference between a structure and a class?
* Structure default access type is public, class’s is private
* Structure is used for grouping data; class groups data and methods

## Virtual function
* A member function you expect to be redefined in derived classes


## What is a pure virtual function?
* A function which can be overridden in the derived class but can’t be defined
* Declared pure by setting function equal to zero
```javascript
         virtual void function() = 0
```				

[https://www.includehelp.com/cpp-tutorial/cpp-interview-questions-and-answers-1.aspx
](https://www.includehelp.com/cpp-tutorial/cpp-interview-questions-and-answers-1.aspx
)

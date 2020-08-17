# Front End Questions

## What are some ways to deal with a slow webpage

### Enable compression
  
### Minify CSS, JavaScript, HTML

* Remove code comments, formatting, unused code
* Tools: CSSNano, UglifyJS

## MVC Model
* Model, View, Controller Model
* Idea => each code section has a different purpose

#### Model
* corresponds to all the data-related logic that the user works with

#### View
* the View component is used for all the UI logic of the application

#### Controller
* Controllers act as an interface between Model and View components to process all the business logic and incoming requests, manipulate data using the Model component and interact with the Views to render the final output


## JSON vs XML

### Difference
* JSON just a data format while XML is a markup language
  *  metadata and attributes can be added in XML

### JSON
* JavaScript Object Notation
* Requires less coding, has smaller size => faster to process and transmit data
* Doesn't have validation/schema related features of XML

#### Features
* Usage is straightforward
* Better performance
  *  consumes little memory
* No dependency

#### Pros
* Supports all browsers
* Creation/manipulation is easy

#### Cons
* offers poor extensibility as no namespace support

### XML
* Extensible Markup Language
* Almost every langauge has a parser for it
* Easy to fetch particular data
* Schemas can validate the XML

#### Pros
* Exchange of data is done quickly between different platforms
* XML separates the data from HTML

#### Cons
* XML requires a processing application
* XML syntax can sometimes be confusing as it is similar to other alternatives
* No intrinsic data type support
* The XML syntax is redundant

## REST vs SOAP

#### Reference
[https://raygun.com/blog/soap-vs-rest-vs-json/](https://raygun.com/blog/soap-vs-rest-vs-json/)

# Web Networking

## API
* Application Program Interface

## REST
* Representational State Transfer
* A software architectural style that defines a set of constraints to be used for creating web services
* Relies on stateless, client-server protocol, almost always HTTP
* Principles:
  *  Client-Server
  *  Layered system
  *  Stateless
  *  Code on demand
  *  Cacheable
  *  Uniform interface
* In a RESTful web service, requests made to a resource’s URI will elicit a response with a payload formatted in HTML, XML, JSON
  *  URI (Uniform Resource Identifier)
* A string of characters that identifies a particular resource
* A response can confirm that some altercation has been made to the stored resource, and the response can provide hypertext links to other related resources
* Hypertext: text displayed with references (hyperlinks) to other text the reader can access
* Hypertext documents are interconnected by hyperlinks
* Scalability 
* Client-server separation of concerns simplifies component implementation, reduces complexity of connector semantics, improves effectiveness of performance tuning, increases scalability of pure server components

## REST Architecture
* Client Server
  *  Each have a different set of concerns
  * Server
    *  Stores/manipulates information and makes it available to user in efficient way
  * Client
    *  Takes info and displays it to user and uses it to perform subsequent requests for information
* Stateless
  *  Server does NOT store any state about client session on the server side
  *  Each request from the client to server must contain all info necessary to understand the request
  *  Client is responsible for sending any state info to server when it’s needed
* Chacheable
  *  Cache resources in order to improve performance

Uniform Interface
Layered System
Code on Demand


## HTTP Methods

### Get
* Retrieve data from a specified resource

### Post
* Submit data to be processed to a specified resource

### Put
* Update a specified resource

### Delete
* Delete a specified resource

### Head
* Same as get but does not return a body 

### Options
* Returns supported HTTP methods

### Patch
* Update partial resources


### Benefits
* Network performance
  * Efficiency
    * Caches help speed up
  * Scalability
    * Caches helps be reducing load on server from increased requests
  * User perceived performance 



## HTML (Hyptertext Markup Langauge)

## CDN (Content Delivery Network)
* A geographically distributed network of proxy servers and their data centers
* Proxy Server
* A server that acts as an intermediary for requests from clients seeking resources from other servers
* Client will connect to proxy server, request some service (file, connection, web page) available from a different server 
* Proxy server evaluates the request (simplifies + controls complexity)
* Adds structure and encapsulation to distributed systems


# Full Stack Interview Questions

### What is multithreading?

Improve CPU performance with multi-threading. A program can manage multiple requests with the same user and can manage many users at the same time. Multiple processes are executed at the same time to improve the performance.

### What is continuous integration?

Merge the working copies of all developers to one shared mainline a few times a day. This helps with easy problem detection. 

Continuous Integration (CI) is the process of automating the build and testing of code every time a team member commits changes to version control. CI encourages developers to share their code and unit tests by merging their changes into a shared version control repository after every small task completion. Committing code triggers an automated build system to grab the latest code from the shared repository and to build, test, and validate the full master branch (also known as the trunk or main).

CI emerged as a best practice because software developers often work in isolation, and then they need to integrate their changes with the rest of the team’s code base.  Waiting days or weeks to integrate code creates many merge conflicts, hard to fix bugs, diverging code strategies, and duplicated efforts.  CI requires the development team’s code be merged to a shared version control branch continuously to avoid these problems.

### What is continuous delivery?

Continuous Delivery (CD) is the process to build, test, configure and deploy from a build to a production environment. Multiple testing or staging environments create a Release Pipeline to automate the creation of infrastructure and deployment of a new build. Successive environments support progressively longer-running activities of integration, load, and user acceptance testing. Continuous Integration starts the CD process and the pipeline stages each successive environment to the next upon successful completion of tests.

#### Resources

[https://docs.microsoft.com/en-us/azure/devops/learn/what-is-continuous-integration](https://docs.microsoft.com/en-us/azure/devops/learn/what-is-continuous-integration)

### Explain CORS?

Cross-Origin Resource Sharing known as CORS, allows you to request for different resources from a different domain outside of the domain where the resource is originally from.

### How to reduce load time of web application?

Minimize HTTP requests, optimizing images, reducing redirects, enabling browser caching are some methods to reduce the load time of web apps. 

### What is an Application server?

An application that lets you design and maintain server side as well as client side application. 

### If you were to write an endpoint for checking if a resource exists, what path and method would you use?

Question purpose => test knowledge of RESTful API standards. 

You wouldn't create an endpoint such as 
```javascript
GET /users/search

GET /users/create
```

Problem with above is the path should only container nouns. The method (GET, POST) should determine the action.

```javascript
POST /users (create a user model
PUT /users/{id} (replace a user model)
DELETE /users/{id} (delete a user model)
GET /users/{id} (retrieve a user model)
```







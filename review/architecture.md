# Architecture

## Microservices
* Allows  developers to create separate components of an application through building an application from a combination of small services
* Each service is built individually and deployed separately
  * Run their own processes
  * Communicate via lightweight APIs
* Make it easier to test, understand, maintain application builds

### Benefits

#### Isolation
* If one component fails, devs have options to use another service and application will continue to run

## Service Mesh
* An inter-service communication infrastructure
* A given Microservice won’t directly communicate with the other microservices
* Rather all service-to-service communications will take places on-top of a software component called service mesh (or side-car proxy)
* Service Mesh provides built-in support for some network functions such as resiliency, service discovery etc.
* Therefore, service developers can focus more on the business logic while most of the work related to network communication is offloaded to the service mesh

#### References
[Medium: Service Mesh for Microservices](https://medium.com/microservices-in-practice/service-mesh-for-microservices-2953109a3c9a)

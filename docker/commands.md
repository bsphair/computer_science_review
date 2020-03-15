# Docker Commands

## Docker run
* Docker runs processes in isolated containers
* A container is a process which runs on a host
* When `docker run` is used, the container process that runs is isolated and has its own file system, networking, processes from the host

* Basic form: 
  * `$ docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]`
  * Must specify an IMAGE from which to derive the container

* Detached vs foreground
  * Defaults to foreground mode
  * `-d` or `-d=true` will make container run in background

### References
* [https://docs.docker.com/engine/reference/run/](https://docs.docker.com/engine/reference/run/)
  
## References
* [https://docs.docker.com/reference/](https://docs.docker.com/reference/)

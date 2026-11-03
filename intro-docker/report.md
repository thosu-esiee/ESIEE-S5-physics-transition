# Cloud Computing - Getting started with docker

Théo Constant E5INFO

## Introducing Containers

The Debian container stopped imediatly after being executed.

`sudo docker ps -l`
```
CONTAINER ID   IMAGE                COMMAND   CREATED         STATUS                     PORTS     NAMES
7e80cb20630e   debian:trixie-slim   "bash"    3 minutes ago   Exited (0) 3 minutes ago             upbeat_hofstadter
```

CONTAINER ID is the id of the container
IMAGE is the name of the image used for this container
COMMAND is 
CREATED is
STATUS is
PORTS is
NAMES is

An image is like a class, while a container is like an instance or object of this class.

`docker run` try to create the container by searching the image localy first and if it does not find the it localy, docker downloads it first, then it start it. `docker start` only tries to start a container already created.

`-i` or `--interactive=true|false` keep STDIN open even if not attached. By default it is false. (from the man page)

`-t` or `--tty=true|false` allocate a pseudo-TTY. By default it is false. When set to true, Docker allocate a pseudo-tty and attach to the standard input of any container. This can be used to run a throwaway interactive shell for exemple. (from the man page)

together, `-it` or `--interactive --tty` can be used to have an interactive terminal inside the container.

If you omit `-it` with the debian image, it is not possible to interact with debian through a tty and it stop running after being started. It should not apply to every image, because some image might have some services that would keep the container alive.

To stop a container, you can use the `docker stop container <name>` command. To remove a stopped container you can use the `docker container rm <name>` command.

## Running a web server

`-d` or `--detach=true|false` allows to run the container in detached mode, in the background

`-it` is not necessary because it is a server, it is waiting for connections, so no need to use `-it` to keep it alive.

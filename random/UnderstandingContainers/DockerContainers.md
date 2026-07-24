Docker Containers and Kubernetes Fundamentals – Full Hands-On Course
https://www.youtube.com/watch?v=kTp5xUtcalw

Setup: 4:00
Visual Studio Code
Docker Desktop with Kubernetes enabled
A Docker Hub account
tools: https://github.com/K8sAcademy/Fundamentals-HandsOn/blob/main/K8sFundamentals-SetupGuide-V3.pdf
Download the lab files here: https://github.com/K8sAcademy/Fundamentals-HandsOn

28:00 Containers Concepts
Containers are made of layers
Base OS
Customisations
Application

One of the goals is to have as little layers as possible.
The top is read/write the ones under that are read only

30:00 What is Docker
An open source container runtime
"Dockerfile" file format for building container images

32:30 Install docker
Install Docker Desktop
https://docs.docker.com/desktop/setup/install/linux/archlinux/

    Install the Docker client binary on Linux.
    https://docs.docker.com/engine/install/binaries/#install-daemon-and-client-binaries-on-linux
     Static binaries for the Docker client are available for Linux as docker. You can use:

     wget https://download.docker.com/linux/static/stable/x86_64/docker-29.4.3.tgz -qO- | tar xvfz - docker/docker --strip-components=1
     sudo cp -rp ./docker /usr/local/bin/ && rm -r ./docker

    Download the latest Arch package from the Release notes.
    https://docs.docker.com/desktop/release-notes/

    Install the package:

     sudo pacman -U ./docker-desktop-x86_64.pkg.tar.zst

    By default, Docker Desktop is installed at /opt/docker-desktop.

Used the wget and cp commands, think installed Docker client binary or cli application
Downloaded docker-desktop to /home/lucas/Documents/DockerLearning/Fundamentals-HandsOn-main/docker-desktop-x86_64.pkg.tar.zst
next use pacman to install the package. something went wrong, updating system and I will try again.  Worked but could have just needed a restart.

docker-desktop/setting/Kubernetes/Enable Kubernetes

36:50 Docker CLI Management Commands

docker info Display system information
docker version Display the system's version
docker login Log in to a Docker registry

40:00 [Docker CLI Running Containers](https://youtu.be/kTp5xUtcalw?t=2410)
[CLI commands](Fundamentals-HandsOn-main/L05-04%20Running%20Containers/Readme.md)

docker run [imageName] Creates a container instance from a image and run it.  If the image file is not local will try to pull from repositories.
docker start [containerName] Starts a stopped instance.
imageName is what comes from repository or made.
containerName is the name of the running instance container.

You can set limits on the memory and cpus of a container can use.
docker run --memory="256" nginx Max memory
docker run --cpus=".5" nginx Max CPU

![running a container](runningContainer.png)

43:14 Docker CLI Cheat Sheet - Attach Shell
Can attach a shell to a container so you can run command in it.
docker run -it nginx -- /bin/bash Attach bash shell
 -i, --interactive       Keep STDIN open even if not attached
      --ip ip            IPv4 address (e.g., 172.30.100.104)
      --ip6 ip           IPv6 address (e.g., 2001:db8::33)
      --ipc string       IPC mode to use
      --isolation string Container isolation technology
-t, --tty                Allocate a pseudo-TTY
      --ulimit ulimit    Ulimit options (default [])
      --use-api-socket   Bind mount Docker API socket and required auth
docker container exec -it [container name] bash Attach to a running container
exec Execute a command in a running container.
  -i, --interactive      Keep STDIN open even if not attached
      --privileged       Give extended privileges to the command
  -t, --tty              Allocate a pseudo-TTY
the terminal prompt will change when attached to a container

docker rm [container name] Removes stopped containers
docker rm $(docker ps -a -q) Removes all stopped containers
docker images List images
docker rmi [image name] Deletes the image
docker system prune -a Removes all images not in use by any containers

45:00 
markdown link local files [name] (path/file) spaces in URLs use %20 or <> for ones containing spaces.

51:22 [Building](Fundamentals-HandsOn-main/L05-06%20Build%20an%20image/Readme.md)

docker build -t [name:tag] . Builds an image using a Dockerfile located in the same folder
docker build -t [name:tag] -f [file name] Builds an image using a Dockerfile located ina different folder
docker tag [image name] [name:tag] Tag an existing image

Dockerfile

A dockerfile is a set of instruction for creating a image.
"it's a text file listing the steps to build an image"

FROM base is made from
COPY to copy from first argument to second, in the container.

dockerfile - Node site
FROM alpine
RUN apk add -update nodejs nodejs-npm 
COPY . /src
WORKDIR /src
RUN npm install
EXPOSE 8080
ENTRYPOINT ["node". ".app.js"]

dockerfile syntax from gemini
The basic syntax follows the format INSTRUCTION arguments
General Rules
Instructions are case-insensitive, but uppercase is standard convention to distinguish them from arguments.
Lines starting with # are treated as comments and ignored.
Instruction are executed in they appear.  Each instruction creates a new image layer.
Specialised comments like #syntax=docker/dockerfile:1 can be placed at the very top to specify the parser version.
FROM Defines the base image for the build
RUN Executes commands in a new layer during the build process (e.g., installing packages).
CMD Provides defaults for an executing container. Only one CMD instruction is effective.
COPY Copies local files or directories into the image's filesystem.
ADD Similar to COPY, but can also handle remote URLs and auto-extract tar archives.
ENV Sets environment variables that persist in the final image.
EXPOSE Documents which ports the container intends to listen on at runtime.
WORKDIR Sets the working directory for subsequent instructions.
ENTRYPOINT Configures a container that will run as an executable.
ARG Defines variables that users can pass at build-time using --build-arg .
Example Dockerfile
# syntax=docker/dockerfile:1
FROM python:3.13
WORKDIR /usr/local/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
EXPOSE 8080
CMD ["python", "src/main.py"]

dockertag

vs code https://www.youtube.com/watch?v=kTp5xUtcalw&t=3281s
vs code to containerise a node js express application https://youtu.be/kTp5xUtcalw?t=3468

[Persisting data](https://youtu.be/kTp5xUtcalw?t=4031)
Containers are ephemeral and stateless, they do have a locally writable layer, but when they are destroyed so is the data inside them.
Persistent Data
Data to persist needs to stored outside the container in a volume.
A volume is mapped to a logical folder.
Your application sees the volume just like a regular folder, it maps to a folder on the host.

## How to create volumes
needs to attach volume when the container instance is created
Volumes Cheat Sheet
docker create volume [volumeName] Creates a new volume
docker volume ls List the volume
docker volume inspect [volumeName] Display the volume information
docker volume rm [volumeName] Deletes volume
docker volume prune Deletes all volumes not mounted

https://youtu.be/kTp5xUtcalw?t=4154

# create a volume
docker volume create myVolume
# inspect the volume
docker volume inspect myVolume The Mountpoint : value shows where it is stored on host.
# run a container with a volume
docker run -d --name devtest -v myVolume:/app nginx:latest
 docker run -d Runs container in detached mode.
  --name devtest Names the container or instance devtest.
   -v myVolume:/app Flag -v maps the created myVolume on the host to /app folder in the container.
    nginx:latest Uses the latest nginx image when creating the container.
Can also map to a local folder
docker run -d --name devtest -v d:/test:/app nginx:latest

https://youtu.be/kTp5xUtcalw?t=4261

https://youtu.be/kTp5xUtcalw?t=4260
# Connect to the container/instance and run bash
docker exec -it [containerName] bash Command exec executes bash with the i and t flags interactive and TTY sets a terminal interface
Then ls to see if in container, then add a file to see if it persists.
 #Install nano
 apt-get update
 apt-get install nano
 #Create file in app folder
 cd app
 nano test.txt
 #Type something
 #Save
 Ctrl + o 
 #Close nano
 Ctrl + x
 #Stop the terminal session
 exit
 #Stop container/instance
 docker stop devtest
 #All data that is in the container/instance is goes away when stopped, unless it is saved in a volume.
 #When starting the container the text file will be there.
## exercise
create a volume, create a container instance and attach the volume, make a file in the container's volume, remove the container, create a container instance check if the file is there, remove the container, create a container instance with the volume, check if the file is there.
docker volume create aVolume
docker run -d --name testVolume -v aVolume:/app nginx:latest
docker exec -it testVolume bash
mkdir app
touch app/hello.txt
exit
docker stop testVolume
docker rm testVolume
docker run -d --name testVolume nginx:latest
docker exec it testVolume bash
ls ( there should not be app folder or hello.txt )
docker stop testVolume
docker rm testVolume
docker run -d --name testVolume -v aVolume:/app nginx:latest
docker exec it testVolume bash
ls ( there should be the app folder and hello.txt ) 
Worked as expected

#YAML:YAML Ain't Markup Language
Human friendly data serialisation standard
Used by Docker-Compose and Kubernetes

key value pair is the keyName colon space theValue 
key: value

associative array is key colon newline space (convention two) key: value
a_nested_map:
  key: value
  another_key: Another Value
  another_nested_map:
    hello: hello

list is key colon newline, each item on a new line denoted by leading hyphen then a space and the value.
a_sequence:
  - Item 1
  - Item 2

Flow style can use json

Linters are good to use to avoid mistakes www.yamllint.com

Docker Compose Concepts
https://youtu.be/kTp5xUtcalw?t=4756
Applications can require multiple containers like, frontend, backend and database.  Instead of using three docker run commands, use a docker compose CLI plugin.  It defines and runs multi-containers applications, define using YAML files.

Docker Compose Example

version: '3.9'

services: 
  webapi1: 
    image: academy.azurecr.io/webapi1
    ports: 
      - '8081:80'
    restart: always

  webapi2:
    image: academy.azurecr.io/webapi2
    ports: 
      - '8082:80'
    restart: always

  apigateway: 
    image: academy.azurecr.io/apigateway
    ports: 
      - '80:80'
    restart: always

There are three entries in services, each is a container and the key of the entry defines the hostname name of the container instance.  image: value is the image, like docker run can be a name of an image and it will look in docker cache or a hub, or a location like above.  ports: listening port

Docker Compose Commands
https://youtu.be/kTp5xUtcalw?t=5000

Docker Compose Cheat Sheet
docker compose build Build the images -f flag to use specify name and file path of one or more compose files
docker compose start Start the containers
docker compose stop Stop the containers
docker compose up -d Build and start, -d flag for detached
docker compose --project-name projectTwo up -d Build another instance called projectTwo
docker compose -p projectTwo up -d Builds another instance with -p project flag
docker compose ps List what is running
docker compose rm Remove from memory
docker compose down Stop and remove
docker compose logs Get the logs
docker compose exec [container] bash Run a command in a container
docker compose ls List running projects
docker compose cp [containerID]:[src_path] [dest_path] Copy files from the container
docker compose cp [scr_path] [containerID]:[dest_path]

port conflicts.
Have a list of ports.
Use Dynamic Host Ports, just assign the containers port.
Usual way is to map container's port to host's port
    ports: 
    - host_port:container_port
services:
  adminer:
    image: adminer
    restart: always
    ports: 
    - 8080:8080
----
Use dynamic host ports
    ports: 
    - 8080

One container can talk to another using the service name, connected to a network.
Usage  
docker network connect [options] NETWORK CONTAINER
docker network connect multi-host-network container1

Docker compose lab
https://youtu.be/kTp5xUtcalw?t=5220
Deploy a docker compose application

`
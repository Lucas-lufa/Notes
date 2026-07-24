https://leantime.io/
https://github.com/Leantime/leantime
Will do two ways docker and docker compose
For docker
https://hub.docker.com/r/leantime/leantime
Create a leantime container, To run this image you will database MySQL

docker run -d -p 80:8080
-e LEAN_DB_HOST=mysql_leantime \
-e LEAN_DB_USER=admin \
-e LEAN_DB_PASSWORD=321.qwerty \
-e LEAN_DB_DATABASE=leantime \
--name leantime leantime/leantime:latest

Will create an container instance with detach (run container in background and print container ID) publish - host_port:container_port 80:8080 (publish a container's port(s) to the host) env (set environment variables) flags, container named leantime, image to use leantime latest in leantime repository.
Any of the environment variables set with the -e flag can configured in config/configuration.php (assume in the container) Once the leantime container instance is running go to <yourdomain.com>/install and run the installation script.

Set up network and database
Create the network so Leantime can communicate with database container (MySQL)

docker network create leantime-net

creates a network called leantime-net

docker run -d -p 3306:3306 --network leantime-net \
-e MYSQL_ROOT_PASSWORD=321.qwerty \
-e MYSQL_DATABASE=leantime \
-e MYSQL_USER=admin \
-e MYSQL_PASSWORD=321.qwerty \
--name mysql_leantime mysql:5.7 --character-set-server=utf8 --collation-server=utf8_unicode_ci

Will create an container instance with ; detach (run container in background and print container ID) ; publish - host_port:container_port 3306:3306 (publish a container's port(s) to the host) ; --network leantime-net (network flag adds the container to the leantime-net docker network) ; env (set environment variables) flags ; container named mysql_leantime ; image to use mysql version 5.7 ; --character-set-server sets the default character set of the MySQL server to utf8 ; --collation-server sets the collation for the MySQL server, which controls how text comparisons work, utf8_unicode_ci utf8 -> the character set it works with, unicode -> uses Unicode sorting rules, ci -> case-insensitive.
Create the Leantime container

docker run -d -p 80:8080 --network leantime-net \
-e LEAN_DB_HOST=mysql_leantime \
-e LEAN_DB_USER=admin \
-e LEAN_DB_PASSWORD=321.qwerty \
-e LEAN_DB_DATABASE=leantime \
--name leantime leantime/leantime:latest

Will create an container instance with ; detach (run container in background and print container ID) ; publish - host_port:container_port 80:80 (publish a container's port(s) to the host) ; --network leantime-net (network flag adds the container to the leantime-net docker network) ; env (set environment variables) flags ; container named leantime ; image to use leantime latest in leantime repository.
Any of the environment variables set with the -e flag can configured in config/configuration.php (assume in the container) Once the leantime container instance is running go to <yourdomain.com>/install and run the installation script.

Full Set up with docker-compose

git clone https://github.com/Leantime/docker-leantime.git
cd docker-leantime
docker-compose up -d
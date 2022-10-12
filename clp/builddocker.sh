### This objective of this file is to use a shell script to build a docker image based on the dockerfile template
### The docker container created can have the default port modified
hostport = 5432
containerport = 5432

docker build -t dockerfile .
docker run --name postgresclp -p $hostport:$containerport dockerfile

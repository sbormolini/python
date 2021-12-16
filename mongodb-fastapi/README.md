# mongodb-fastapi sample

A Bare Bones Slack API
Illustrates basic usage of FastAPI with MongoDB


### run docker mongo db 

>docker run --name my_mongo -p 27017:27017 -d mongo:latest

### docker build image and run
>docker build --pull --rm -f "Dockerfile" -t mongodbfastapi:latest "."

>docker run --rm -dp 5000:5000/tcp mongodbfastapi:latest


### docker compose
>docker-compose -f "docker-compose.yml" up -d --build
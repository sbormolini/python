# Using lightweight alpine image
FROM python:3.9-alpine

# Installing packages
RUN apk add curl
RUN apk update
RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /usr/src/python-docker-sample
COPY /src/Pipfile /src/Pipfile.lock /src/bootstrap.sh ./
COPY /src/api.py ./

# Install API dependencies
RUN pipenv install

# Start app
EXPOSE 5000
ENTRYPOINT ["/usr/src/python-docker-sample/bootstrap.sh"]
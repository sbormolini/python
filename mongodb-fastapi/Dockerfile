# python base image in the container from Docker Hub
FROM python:3.7.9-slim

# copy files to the /app folder in the container
COPY ./src/main.py /app/
COPY ./src/Pipfile /app/
COPY ./src/Pipfile.lock /app/
COPY ./src/models /app/models

# set the working directory in the container to be /app
WORKDIR /app

# install the packages from the Pipfile in the container
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

# set python path
ENV PYTHONPATH "${PYTHONPATH}:/app/"

# expose the port that uvicorn will run the app on
ENV PORT=5000
EXPOSE 5000

# execute the command python main.py (in the WORKDIR) to start the app
CMD ["python", "main.py"]
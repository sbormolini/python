# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9-appservice
FROM mcr.microsoft.com/azure-functions/python:3.0-python3.9

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

# Install Chromium
RUN apt-get install chromium -y

# Set up Chromedriver Environment variables
#ENV CHROMEDRIVER_VERSION 2.19
#ENV CHROMEDRIVER_DIR /chromedriver
#RUN mkdir $CHROMEDRIVER_DIR

# Download and install Chromedriver
#RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
#RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /home/site/wwwroot
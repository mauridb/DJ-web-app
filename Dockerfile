# base image
FROM ubuntu:latest

# commands to run to install package for the image
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python-pip

# create application dir
WORKDIR /app

# install project dependencies
COPY requirements/production/prod_requirements.txt prod_requirements.txt
RUN pip install -r prod_requirements.txt

# Make port available
EXPOSE 8080
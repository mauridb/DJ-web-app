# base image
FROM ubuntu:latest

# commands to run to install package for the image
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y git

# create application dir
WORKDIR /app/

# install project dependencies
RUN git clone -b dockerfile https://github.com/mauridb/DJ-web-app.git
RUN pip3 install -r DJ-web-app/requirements/production/prod_requirements.txt


# Make port available
EXPOSE 8080
# base image
FROM ubuntu:latest

# commands to run to install package for the image
RUN apt-get update -y
RUN apt-get install -y python-pip && pip install --upgrade pip
RUN apt-get install -y git



# create application dir
WORKDIR /app/

# install project dependencies
RUN git clone -b release https://github.com/mauridb/DJ-web-app.git
RUN pip install -r DJ-web-app/requirements/production/prod_requirements.txt

WORKDIR DJ-web-app/

RUN sleep 10

# when you pass commands to the container
ENTRYPOINT ["python"]

# launch below command when run container
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

# Make port available
#EXPOSE 8000
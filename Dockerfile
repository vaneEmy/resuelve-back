FROM python:3.9-alpine

# RUN PYTHON WITHOUT BUFFER
ENV PYTHONUNBUFFERED 1

# INSTALL LIBSSL-DEV, GCC
RUN apk add libressl-dev build-base 

# Copy our requirements file to the container
COPY ./requirements.txt /requirements.txt

# Install all dependecies that the requirements file has.
RUN pip install -r /requirements.txt

# Copy our app to docker container
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Create a user that is going to run our application using docker
RUN adduser -D user
USER user

# pull official base image
FROM python:3.9-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get install -y netcat-openbsd gcc \
  && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ../requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY .. .

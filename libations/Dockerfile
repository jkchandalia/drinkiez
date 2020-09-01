
# pull official base image
FROM python:3.7.2-slim

# set work directory
WORKDIR /usr/src/libations

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /usr/src/libations/staticfiles

# copy project
COPY . .


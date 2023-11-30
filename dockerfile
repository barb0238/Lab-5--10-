FROM python:3.11.2-slim-buster

RUN mkdir -p /usr/src/app
# this might not be necessary
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
# prevents python from writing pyc files to disc 
ENV PYTHONBUFFERED 1
# prevents python from buffering stdout and stderr

#install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean


COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh .
RUN  /usr/src/app/entrypoint.sh 


FROM python:3.11.2-slim-buster

RUN mkdir -p /usr/src/app
# this might not be necessary
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
# prevents python from writing pyc files to disc 
ENV PYTHONBUFFERED 1
# prevents python from buffering stdout and stderr

# new
# install system dependencies
RUN apt-get update \
&& apt-get -y install netcat gcc postgresql \
&& apt-get clean
# add and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# add app
COPY . .

# new
# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh
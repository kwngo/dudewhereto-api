FROM python:3.6
MAINTAINER Kareem

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# -- Install dependencies:
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv

# 1. install pipenv and create an entrypoint 
RUN echo "#!/bin/bash" >> /entrypoint.sh && \
    echo 'exec "$@"' >> /entrypoint.sh && \
    chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# <-- system level dependencies here
RUN apt-get update
RUN apt-get install -y git htop vim wget net-tools dialog gunicorn
RUN apt-get install -y nginx

# 3. don't run as root
RUN groupadd --gid 1001 docker
RUN useradd --uid 1001 --gid docker --home /app kwngo
RUN mkdir /app && chown kwngo.docker /app


WORKDIR /app

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# -- Adding Pipfiles
RUN set -ex && pipenv install --deploy --system --dev

USER kwngo
COPY . /app

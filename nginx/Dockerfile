FROM nginx
MAINTAINER Kareem

RUN apt-get update
RUN apt-get install -y vim wget net-tools dialog
COPY nginx.conf /etc/nginx/nginx.conf

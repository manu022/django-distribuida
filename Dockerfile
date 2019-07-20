FROM phusion/baseimage
MAINTAINER distribuida
 
ENV DEBIAN_FRONTEND noninteractive
 
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev
RUN apt-get install -y libxml2-dev libxslt-dev libffi-dev libssl-dev
RUN apt-get install -y libmysqlclient-dev
 
ADD requirements.txt /app/src/requirements.txt
WORKDIR /app/src
RUN pip install -r requirements.txt
 
WORKDIR /app/src/lisp
CMD [ "python", "manage.py", "runall"]
 
EXPOSE 8000

FROM python:3.6-slim
ARG webapp_env
ENV webapp_env=${webapp_env}

# Creating app directory
WORKDIR /webapp

# Installing dependencies before copying the app code allow the use of docker
# cache when rebuilding the image after a code change
COPY requirements /webapp/requirements

# uwsgi requires gcc, if you don't use uwsgi you can remove this line
RUN apt-get update && apt-get install -y gcc

RUN pip install -r "requirements/$webapp_env.txt"

COPY . /webapp/

RUN cd /webapp/ && \
    chmod a+x docker_entrypoint.sh && \
    DJANGO_SETTINGS_MODULE=server.settings.$webapp_env python manage.py collectstatic --noinput

EXPOSE 1704

ENTRYPOINT "/webapp/docker_entrypoint.sh"

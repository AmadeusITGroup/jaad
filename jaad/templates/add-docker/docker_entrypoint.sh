#!/bin/bash
# shellcheck disable=SC2154

mkdir -p "$log_folder/$HOSTNAME"

uwsgi \
 --ini webapp.ini\
 --env "DJANGO_SETTINGS_MODULE=server.settings.$webapp_env"\
 --logto "$log_folder/$HOSTNAME/uwsgi.log"

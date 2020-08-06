#!/usr/bin/env bash

# use this shell to resolve DJANGO_PORT variable, see https://docs.docker.com/engine/reference/builder/#cmd
# use exec to replace the shell by the specified command, see https://docs.docker.com/compose/startup-order/
exec python manage.py runserver "0.0.0.0:${DJANGO_PORT}"
# commands written from here (after exec) does not run

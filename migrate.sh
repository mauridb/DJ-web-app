#!/usr/bin/env bash

eval "sleep 10"
eval "python manage.py makemigrations"
eval "python manage.py migrate"
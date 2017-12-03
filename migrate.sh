#!/usr/bin/env bash

sleep 10
python manage.py makemigrations
python manage.py migrate
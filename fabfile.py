# -*- coding: utf-8 -*-
from __future__ import with_statement
from fabric.api import *


# TODO: migrate, start, prepare_dev, release, prepare_master


def start():
    local("python manage.py runserver 0.0.0.0:8000")


def migrate():
    local("python manage.py makemigrations")
    local("python manage.py migrate")


def closed(commit_message):
    local("git pull origin develop")
    local("git add .")
    local("git commit -m '{}'".format(commit_message))
    local("git push ")


# fab prepare_develop:'dockerfile'
def prepare_develop(myfeature):
    local('git checkout develop')
    local('git merge -m "CLOSED-FEATURE-{}" {}'.format(myfeature, myfeature))
    local('git push origin develop')
    local('git branch -d {}'.format(myfeature))
    local('git push origin --delete origin/{}'.format(myfeature))
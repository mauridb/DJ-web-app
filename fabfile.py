# -*- coding: utf-8 -*-
from __future__ import with_statement
from fabric.api import *


# TODO: migrate, start, prepare_dev, release, prepare_master


def start():
    local("python manage.py runserver 0.0.0.0:8000")


def migrate():
    local("python manage.py makemigrations")
    local("python manage.py migrate")


# STEP 1
# fab closed_feature:'FIX: little bug fixing'
def closed_feature(commit_message):
    local("git add .")
    local("git commit -m '{}'".format(commit_message))
    local("git pull origin develop")
    local("git push")


# STEP 2
# fab prepare_develop:'dockerfile'
def prepare_develop(myfeature):
    local('git checkout develop')
    local('git merge -m "CLOSED-FEATURE-{}" {}'.format(myfeature, myfeature))
    local('git push origin develop')
    local('git branch -d {}'.format(myfeature))


# STEP 3
def release(tag):
    local('git checkout release')
    local('git merge -m "RELEASED" develop')
    local('git push origin release')
    local('git checkout master')
    local('git tag {}'.format(tag))
    local('git merge -m "merge with release" release')
    local('git push origin --tags master')
    local('git checkout develop')
    local('git pull origin master')


# STEP 4 if true
def closed_fix(commit_message):
    local("git add .")
    local("git commit -m '{}'".format(commit_message))
    local("git pull origin master")
    local("git push")


# STEP 5 if true
# fab bug_fixing:hotfix='login',tag='1.0.2'
def bug_fixing(hotfix, tag):
    local('git checkout master')
    local('git merge -m "HOTFIXING" {}'.format(hotfix))
    local('git tag {}'.format(tag))
    local('git push origin --tags master')
    local('git branch -d {}'.format(hotfix))
    local('git checkout develop')
    local('git pull origin master')
    local('git push origin develop')

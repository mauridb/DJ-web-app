# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    argument = models.CharField(max_length=100, blank=False, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    def __str__(self):
        return "%s" % self.name


class Customer(models.Model):
    web_user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, blank=True, null=True)
    role = models.CharField(max_length=50, choices=CUSTOMER_ROLE_OPTIONS, blank=False, null=False)

    def __str__(self):
        return "%s %s" % (self.web_user.first_name, self.web_user.last_name)


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    guest = models.CharField(max_length=100, blank=False, null=False)
    theme = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    duration = models.DecimalField(decimal_places=2, max_digits=3, blank=True, null=True)  # in hours
    course_date = models.DateTimeField()

    def __str__(self):
        return "%s" % self.theme

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

from web_booking.settings import CUSTOMER_ROLE_OPTIONS


class Course(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)
    argument = models.CharField(max_length=100, blank=False, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()

    @property
    def count_customer(self):
        return self.customer_set.all().count()

    def __str__(self):
        return "%s" % self.name


class Subscription(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    time_booking = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)


class Customer(models.Model):
    web_user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING, blank=True, null=True)
    subscription = models.ForeignKey(Subscription, blank=True, null=True)
    role = models.CharField(max_length=50, choices=CUSTOMER_ROLE_OPTIONS, blank=False, null=False, default='user')
    allow_booking = models.BooleanField(default=True)
    count_disclaimer = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    count_booking = models.IntegerField(default=0)
    disable_date = models.DateTimeField(blank=True, null=True)
    enable_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.web_user.first_name, self.web_user.last_name)


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=False)
    guest = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, blank=False, null=False)
    theme = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    duration = models.DecimalField(decimal_places=2, max_digits=3, blank=True, null=True)  # in hours
    lecture_date = models.DateTimeField(null=True)
    max_attendees = models.IntegerField(blank=False, null=False)
    booked_participants = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.theme


class Booking(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.DO_NOTHING, blank=False, null=False)
    lecture = models.OneToOneField(Lecture, on_delete=models.DO_NOTHING, blank=False, null=False)
    booking_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}_{}_{}_{}".format(self.pk, self.customer, self.lecture, self.booking_date)


class News(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=500, blank=False, null=False)
    news_date = models.DateTimeField()

    def __str__(self):
        return "{}_{}".format(self.title, self.news_date)

    class Meta:
        verbose_name_plural = "News"
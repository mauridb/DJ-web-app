# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customer, Lecture, Course, Subscription, Booking, News


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('web_user', 'course', 'subscription', 'role', 'allow_booking', 'count_disclaimer')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'argument', 'description', 'started_at', 'ended_at', 'count_customer')

admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Subscription)
admin.site.register(Booking)
admin.site.register(News)



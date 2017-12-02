# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Customer, Lecture, Course

# Register your models here.
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Customer)

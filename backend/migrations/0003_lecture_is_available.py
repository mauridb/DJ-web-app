# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_customer_count_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]

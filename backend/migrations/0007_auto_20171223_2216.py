# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 21:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20171223_2215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-10-18 06:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='address',
        ),
    ]

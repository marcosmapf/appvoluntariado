# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-10-21 05:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20181021_0201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ('trading_name',), 'verbose_name_plural': 'Companies'},
        ),
    ]

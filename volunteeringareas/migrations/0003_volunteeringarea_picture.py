# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-03 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteeringareas', '0002_auto_20181021_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteeringarea',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

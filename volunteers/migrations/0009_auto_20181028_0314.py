# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-28 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0008_auto_20181028_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='interest_areas',
            field=models.ManyToManyField(blank=True, to='volunteeringareas.VolunteeringArea'),
        ),
    ]

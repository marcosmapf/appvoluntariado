# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-10-21 06:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteeringareas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VolunteerArea',
            new_name='VolunteeringArea',
        ),
        migrations.AlterModelOptions(
            name='volunteeringarea',
            options={'verbose_name_plural': 'VolunteeringAreas'},
        ),
    ]
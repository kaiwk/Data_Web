# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-22 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gathering', '0008_datatable_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]

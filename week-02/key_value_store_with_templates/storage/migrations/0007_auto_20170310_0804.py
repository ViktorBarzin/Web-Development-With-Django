# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 08:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0006_remove_user_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyvalue',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

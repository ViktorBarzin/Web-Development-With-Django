# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20170308_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default='8185314f896e4bd9956cc7868db17eaf', primary_key=True, serialize=False),
        ),
    ]

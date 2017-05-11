# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20170420_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='choices',
            field=models.CharField(choices=[('A', 'approved'), ('P', 'pending'), ('R', 'rejected')], default='A', max_length=8),
        ),
    ]
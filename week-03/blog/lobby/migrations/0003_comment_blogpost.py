# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0002_auto_20170316_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blogpost',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='lobby.BlogPost'),
            preserve_default=False,
        ),
    ]
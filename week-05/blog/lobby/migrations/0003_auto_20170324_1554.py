# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 15:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0002_auto_20170324_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentauthor',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='lobby.CommentAuthor'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('users', '0002_user'),
        ('category', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('categories', models.ManyToManyField(related_name='products', to='category.Category')),
                ('comments', models.ManyToManyField(through='comments.Comment', to='users.User')),
            ],
        ),
    ]

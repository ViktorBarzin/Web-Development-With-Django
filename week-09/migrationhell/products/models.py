from django.db import models

import uuid
# from users.models import User
# from category.models import Category
# Create your models here.


class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(unique=True, max_length=255)

    comments = models.ManyToManyField('users.User', through='comments.Comment')
    categories = models.ManyToManyField('category.Category', related_name='products')


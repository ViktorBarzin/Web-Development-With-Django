from django.db import models
import uuid

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey('users.User', related_name='comments')
    product = models.ForeignKey('products.Product')
    text = models.TextField()

# class Meta:
#     managed = False
#     db_table = 'comments_comment'

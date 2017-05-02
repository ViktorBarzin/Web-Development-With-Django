from django.db import models
import uuid

class Category(models.Model):
    name = models.CharField(unique=True, max_length=255)

# class Meta:
#     managed = False
#     db_table = 'category_category'

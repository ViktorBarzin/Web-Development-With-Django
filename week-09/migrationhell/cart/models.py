from django.db import models
# from products.models import Product, Order

import uuid
# Create your models here.


class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey('users.User', related_name='orders')
    products = models.ManyToManyField('products.Product')


class Invoice(models.Model):
    company_data = models.TextField()
    order = models.OneToOneField(Order)


# class Meta:
#     managed = False
#     db_table = ''

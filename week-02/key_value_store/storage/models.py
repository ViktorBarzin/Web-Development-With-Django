from django.db import models

# Create your models here.
import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4().hex)


class KeyValue(models.Model):
    key = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, related_name='key_values', on_delete=None)


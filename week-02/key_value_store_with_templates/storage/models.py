from django.db import models

# Create your models here.
import uuid
from datetime import datetime


class CreatedAtModelMixin(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(default=datetime.now)


class User(CreatedAtModelMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)


class KeyValue(CreatedAtModelMixin):
    key = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, related_name='key_values')


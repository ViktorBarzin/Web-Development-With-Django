from django.db import models
from django.utils import timezone

# Create your models here.

class CreatedAtModelMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        abstract = True


class BlogPost(CreatedAtModelMixin, models.Model):
    title = models.CharField(max_length=255, unique=True)
    updated = models.DateTimeField(default=timezone.now)
    content = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=255)
    blogpost = models.ManyToManyField(BlogPost, related_name='tags')


class Comment(CreatedAtModelMixin, models.Model):
    author_email = models.CharField(max_length=255)
    content = models.TextField()
    blogpost = models.ForeignKey(BlogPost, related_name='comments')




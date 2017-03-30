from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class CreatedAtModelMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        abstract = True


class Author(User):
    pass


class CommentAuthor(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    # Has to be validated
    phone = models.CharField(max_length=50, null=True, blank=True)

class BlogPost(CreatedAtModelMixin, models.Model):
    title = models.CharField(max_length=255, unique=True)
    updated = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    author = models.ManyToManyField(Author, related_name='blogposts', blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=255)
    blogpost = models.ManyToManyField(BlogPost, related_name='tags')

    def __str__(self):
        return self.name


class Comment(CreatedAtModelMixin, models.Model):
    # Not using author model because you don't need to be registered to comment
    # as per current requirements
    # default_author = CommentAuthor(fullname='default', email='default@default.com', phone='1234')
    author = models.ForeignKey(CommentAuthor, related_name='comments', null=True)
    content = models.TextField()
    blogpost = models.ForeignKey(BlogPost, related_name='comments')


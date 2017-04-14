from django.contrib import admin

# Register your models here.
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogPost, BlogPostAdmin)

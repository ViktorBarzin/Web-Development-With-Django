from django.conf.urls import url
from .views import index_view, create_blogpost_view, blogpost_info_view


urlpatterns = [
    url(r'^$', index_view, name='index'),
    # Creating posts is done via admin panel
    url(r'^create-post/$', create_blogpost_view),
    url(r'^blog/(?P<blog_id>[0-9]+)/$', blogpost_info_view, name='blog_info')
]

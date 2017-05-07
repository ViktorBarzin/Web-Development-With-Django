
from django.conf.urls import url, include
from downloader import urls as downloader_urls
from .views import index_view, download_file_view, thankyou_view

uuid_pattern = '[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12}'

urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^download/(?P<pk>{})'.format(uuid_pattern), download_file_view, name='download_file'),
    url(r'^thank-you/$', thankyou_view, name='thankyou'),
]


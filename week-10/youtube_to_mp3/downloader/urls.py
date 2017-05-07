

from django.conf.urls import url
from .views import download_video_view


urlpatterns = [
    url(r'^', download_video_view, name='download_video'),

]


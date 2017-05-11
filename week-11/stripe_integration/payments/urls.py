from django.conf.urls import url, include
from .views import buy_view

urlpatterns = [
    url(r'^buy/$', buy_view, name='buy'),
    url(r'^create-customer/$', buy_view, name='create-customer')
]

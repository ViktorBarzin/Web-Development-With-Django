from django.conf.urls import url
from .views import register_view, login_view


urlpatterns = [
        url(r'register/$', register_view, name='register'),
        url('login/$', login_view, name='login')
]

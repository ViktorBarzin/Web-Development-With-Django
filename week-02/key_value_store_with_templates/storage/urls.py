from django.conf.urls import url
from storage.views import home_view, user_detail_view, add_key_view



urlpatterns = [
    url(r'^$', home_view),
    # url(r'^(?P<identifier>{})'.format(uuid_regex), user_detail_view),
]

from django.conf.urls import url, include
from .views import create_user_view, store_data_view, get_key_view, manage_key_view

# 12597158-9a19-4c46-aa90-7f4f28beda57
uuid_regex = r'[\w\d]{8}\-[\w\d]{4}\-[\w\d]{4}-[\w\d]{4}\-[\w\d]{12}'
patterns = [
    url(r'^create-user', create_user_view),
    url(r'^(?P<identifier>{})/$'.format(uuid_regex), store_data_view),
    url(r'^(?P<identifier>{})/(?P<key>[^/]+)/$'.format(uuid_regex), manage_key_view)
]

urlpatterns = [
    url('^storage/', include(patterns))
]

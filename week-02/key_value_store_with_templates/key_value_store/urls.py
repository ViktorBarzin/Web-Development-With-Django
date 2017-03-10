from django.conf.urls import url, include
from django.contrib import admin

from storage.views import add_key_view, user_detail_view

uuid_regex = r'[a-fA-F\d]{8}\-[a-fA-F\d]{4}\-[a-fA-F\d]{4}-[a-fA-F\d]{4}\-[a-fA-F\d]{12}'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^$', include('storage.urls')),
    url(r'^user-detail/(?P<identifier>{})/$'.format(uuid_regex), user_detail_view, name='user-detail'),
    url(r'^add-key/(?P<identifier>{})/$'.format(uuid_regex), add_key_view, name='add_key')

]

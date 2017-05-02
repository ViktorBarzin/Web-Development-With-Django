from django.conf.urls import url
from .views import ListOffersView, OfferDetailView, ListCategoriesView, CategoryDetailView


urlpatterns = [
    url(r'offers/$', ListOffersView.as_view(), name='get-offers'),
    url(r'offers/(?P<pk>[0-9]+)/$', OfferDetailView.as_view(), name='offer-detail'),
    url(r'categories/$', ListCategoriesView.as_view(), name = 'get-categories'),
    url(r'categories/(?P<pk>[0-9]+)/$', CategoryDetailView.as_view(), name='category-detail'),

]

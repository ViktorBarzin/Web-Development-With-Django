from django.conf.urls import url
from django.contrib.auth.views import login, logout
from .views import get_statistics, RegisterView, CreateOfferView, UpdateOfferView, DeleteOfferView, OfferListView, PendingOffersView, ApprovedAndRejectedOffers, RejectOffer, ApproveOffer



urlpatterns = [
    url(r'^$', OfferListView.as_view(), name='index'),
    url(r'^login/$', login, name='login'),
    url(r'register', RegisterView.as_view(), name='register'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^add-offer/$', CreateOfferView.as_view(), name='add-offer'),
    url(r'^offer/edit/(?P<pk>[0-9]+)', UpdateOfferView.as_view(), name='edit-offer'),
    url(r'^delete/(?P<pk>[0-9]+)$', DeleteOfferView.as_view(), name='delete-offer'),
    url(r'^statistics/$', get_statistics, name='statistics'),
    url(r'^offer/pending/$', PendingOffersView.as_view(), name='pending-offers'),
    url(r'^offer/accepted-or-rejected/$', ApprovedAndRejectedOffers.as_view(), name='approved-or-rejected-offers'),
    url(r'offer/approve/(?P<pk>[0-9]+)/$', ApproveOffer.as_view(), name='approve-offer'),
    url(r'offer/reject/(?P<pk>[0-9]+)/$', RejectOffer.as_view(), name='reject-offer'),

]

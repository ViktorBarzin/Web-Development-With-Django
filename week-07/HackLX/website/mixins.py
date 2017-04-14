from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from website.models import Offer


class BaseMixin(UserPassesTestMixin):
    raise_exception = True
    def test_func(self):
        return True


class UserCanUpdateOrDeleteOfferMixin(BaseMixin):
    def test_func(self):
        offer_id = self.kwargs.get('pk')
        offer = get_object_or_404(Offer, pk=offer_id)

        return self.request.user == offer.author and super().test_func()


class LoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('website:login')


class SuperUserRequiredMixin(BaseMixin):
    def test_func(self):
        return self.request.user.is_superuser and super().test_func()

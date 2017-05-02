from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from .forms import CreateOfferModelForm, RegisterModelForm, UpdateOfferModelForm
from .mixins import LoginRequiredMixin, UserCanUpdateOrDeleteOfferMixin, SuperUserRequiredMixin
from .models import Offer, Category



class RegisterView(FormView):

    template_name = 'registration/registration.html'
    form_class = RegisterModelForm
    success_url = reverse_lazy('website:login')

    def form_valid(self, form):
        User.objects.create_user(username=form.data['username'], password=form.data['password'])
        return super().form_valid(form)

class CreateOfferView(LoginRequiredMixin, CreateView):
    model = Offer
    template_name = 'website/add_offer.html'
    form_class = CreateOfferModelForm
    success_url = reverse_lazy('website:index')


    def form_valid(self, form):
        # offer = form.save(commit=False)
        # offer.author = self.request.user

        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateOfferView(LoginRequiredMixin, UserCanUpdateOrDeleteOfferMixin, UpdateView):
    model = Offer
    form_class = UpdateOfferModelForm
    template_name = 'website/add_offer.html'
    success_url = reverse_lazy('website:index')


class DeleteOfferView(LoginRequiredMixin, UserCanUpdateOrDeleteOfferMixin, DeleteView):
    model = Offer
    template_name = 'website/index.html'
    success_url = reverse_lazy('website:index')

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        storage, path = self.object.image.storage, self.object.image.path
        storage.delete(path)
        return super().delete(*args, **kwargs)


class ApproveOffer(LoginRequiredMixin,SuperUserRequiredMixin, RedirectView):
    url = reverse_lazy('website:pending-offers')

    def get(self, *args, **kwargs):
        offer = get_object_or_404(Offer,id=kwargs['pk'])
        offer.choices = 'approved'
        offer.save()
        return super().get(*args, **kwargs)


class RejectOffer(LoginRequiredMixin, SuperUserRequiredMixin, RedirectView):
    url = reverse_lazy('website:pending-offers')

    def get(self, *args, **kwargs):
        offer = get_object_or_404(Offer,id=kwargs['pk'])
        offer.choices = 'rejected'
        offer.save()
        # Delete offer image
        storage, path = offer.image.storage, offer.image.path
        storage.delete(path)
        return super().get(*args, **kwargs)


class OfferListView(ListView):
    model = Offer
    template_name = 'website/index.html'
    paginate_by = 5
    queryset = Offer.objects.order_by('created_at').reverse().filter(choices='A')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].select_related('author', 'category').all()
        return context


class PendingOffersView(ListView):
    model = Offer
    template_name = 'website/pending_offers.html'
    queryset = Offer.objects.filter(choices='pending')


class ApprovedAndRejectedOffers(ListView):
    model = Offer
    template_name = 'website/index.html'
    queryset = Offer.objects.filter(Q(choices='approved') | Q(choices='rejected'))


def get_statistics(request):
    # TODO: Move logic in services
    categories = Category.objects.all()
    categories_result = {}

    for category in categories:
        categories_result[category.name] = category.offer_set.count()


    # TODO: Add more statistics information

    return render(request, 'website/statistics.html', locals())


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from .models import Offer, Category
from .forms import CreateOfferModelForm, RegisterModelForm, UpdateOfferModelForm



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


class UpdateOfferView(LoginRequiredMixin, UpdateView):
    model = Offer
    form_class = UpdateOfferModelForm
    template_name = 'website/add_offer.html'
    success_url = reverse_lazy('website:index')


class DeleteOfferView(LoginRequiredMixin, DeleteView):
    model = Offer
    template_name = 'website/index.html'
    success_url = reverse_lazy('website:index')


class OfferListView(ListView):
    model = Offer
    template_name = 'website/index.html'
    paginate_by = 2
    queryset = Offer.objects.order_by('created_at').reverse()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = context['object_list'].select_related('author', 'category').all()
        return context

def get_statistics(request):
    # TODO: Move logic in services
    categories = Category.objects.all()
    categories_result = {}

    for category in categories:
        categories_result[category.name] = category.offer_set.count()


    # TODO: Add more statistics information

    return render(request, 'website/statistics.html', locals())


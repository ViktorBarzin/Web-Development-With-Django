from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
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

    # TODO: Try to just plugin and add request.user rather override the entire
    # method
    def post(self, request):
        form = CreateOfferModelForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect(reverse('website:index'))
        return render(request, 'website/add_offer.html', locals())


class UpdateOfferView(LoginRequiredMixin, UpdateView):
    model = Offer
    form_class = UpdateOfferModelForm
    template_name = 'website/add_offer.html'
    success_url = reverse_lazy('website:index')

    def form_valid(self, form):
        return super().form_valid(form)


class DeleteOfferView(LoginRequiredMixin, DeleteView):
    model = Offer
    template_name = 'website/index.html'
    success_url = reverse_lazy('website:index')


class OfferListView(ListView):
    model = Offer
    template_name = 'website/index.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Offer.objects.select_related('author', 'category').all()
        return context
        # object_list = 1

def get_statistics(request):
    # TODO: Move logic in services
    categories = Category.objects.all()
    categories_result = {}

    for category in categories:
        categories_result[category.name] = category.offer_set.count()


    # TODO: Add more statistics information

    return render(request, 'website/statistics.html', locals())

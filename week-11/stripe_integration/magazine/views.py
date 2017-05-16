from stripe_integration.settings import STRIPE_PUBLIC_KEY
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Magazine, Article


class MagazineListview(LoginRequiredMixin, ListView):
    model = Magazine
    template_name = 'magazine/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        import ipdb; ipdb.set_trace() # BREAKPOINT
        context['stripe_pk'] = STRIPE_PUBLIC_KEY
        return context


class ArticleListview(ListView):
    model = Article
    template_name = 'magazine/article_list.html'

    def get_queryset(self):
        return self.model.objects\
                         .filter(magazine_id=self.kwargs.get('magazine_id'))

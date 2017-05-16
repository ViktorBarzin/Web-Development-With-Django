from django.shortcuts import render
from stripe_integration.settings import STRIPE_PUBLIC_KEY
import stripe
from .tasks import charge_task


def buy_view(request, *args, **kwargs):
    if request.method == 'POST':
        import ipdb; ipdb.set_trace() # BREAKPOINT

        charge_task.s(request.POST.get('stripeToken')).delay()

    return render(request, 'magazine/list.html', locals())


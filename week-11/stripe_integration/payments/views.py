from django.shortcuts import render
from stripe_integration.settings import STRIPE_PUBLIC_KEY
import stripe


def buy_view(request, *args, **kwargs):
    if request.method == 'POST':
        import ipdb; ipdb.set_trace() # BREAKPOINT
        stripe.Charge.create(
        amount=2000,
        currency="usd",
        source= request.POST.get('stripeToken'),# obtained with Stripe.js
        description="Charge for emma.williams@example.com"
        )

    email = request.user.email
    stripe_pk = STRIPE_PUBLIC_KEY

    return render(request, 'magazine/list.html', locals())

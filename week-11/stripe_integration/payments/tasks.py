from celery import shared_task
import stripe


@shared_task
def charge_task(stripe_token):
#    stripe.api_key = 'sk_test_odAnu62sBKo89QnJwsCyHP7e'
    stripe.Charge.create(
    amount=2000,
    currency="usd",
    source= stripe_token,# obtained with Stripe.js
    description="Charge for emma.williams@example.com"
    )

from .models import User
from django.contrib.auth import authenticate


def validate_user(email, password):
    user = authenticate(username=email, password=password)
    return user

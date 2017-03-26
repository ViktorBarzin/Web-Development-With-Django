from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import login


from .forms import RegisterForm, LoginForm
from .models import User
from .services import validate_user

# Create your views here.

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.data.get('email')
            password = form.data.get('password')
            user = User.objects.create_user(username=email, password=password)
            return redirect(reverse('profile'))

        # import ipdb; ipdb.set_trace() # BREAKPOINT

    return render(request, 'register.html', locals())


def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = form.data.get('email')
        password = form.data.get('password')
        user = validate_user(email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('profile'))
        form.add_error('', 'Login Failed!')
    return render(request, 'login.html', locals())

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from .forms import *


@login_required(login_url='signin')
def account(request):
    return render(request, 'register/account.html')


@login_required(login_url='signin')
def prifile(request):
    template_name = "register/profile.html"
    success_url = "profile"

    if request.method == 'POST':
        data = request.POST
        profile = Profile.objects.get(user=request.user)
        profile.has_profile = True
        form = ProfileForm(data, instance=profile)
        if form.is_valid():
            profile.save()
            form.save()
            return redirect(success_url)
    else:
        form = ProfileForm()
    return render(request, template_name, {"form":form})


def sign_up(request):
    template_name = "register/sign_up.html"
    success_url = "account"

    if request.method == 'POST':
        data = request.POST
        form = SingupForm(data)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=data['username'], password=data['password2'])
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect(success_url)
    else:
        form = SingupForm()
    return render(request, template_name, {"form":form})


def sign_in(request):
    template_name = "register/sign_in.html"
    success_url = "account"

    if request.method == 'POST':
        data = request.POST
        form = SigninForm(data)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            print(user)
            print(User.objects.filter(username=data['username']))
            return redirect(success_url)
    else:
        form = SigninForm()
    return render(request, template_name, {"form":form})


@login_required(login_url='signin')
def sign_out(request):
    logout(request)
    return redirect("/")
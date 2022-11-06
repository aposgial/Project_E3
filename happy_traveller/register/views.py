from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from .forms import *

def sign_up_view(request):
    template_name = "register/sign_up.html"
    success_url = "/"

    if request.method == 'POST':
        data = request.POST
        form = SingupForm(data)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=data['username'], password=data['password2'])
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(success_url)
    else:
        form = SingupForm()
    return render(request, template_name, {"form":form})

def sign_in_view(request):
    template_name = "register/sign_in.html"
    success_url = "/"

    if request.method == 'POST':
        data = request.POST
        form = SigninForm(data)
        if form.is_valid():
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect(success_url)
    else:
        form = SigninForm()
    return render(request, template_name, {"form":form})

def sign_out_view(request):
    logout(request)
    return redirect(request, "register/sign_out.html")
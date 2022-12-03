from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from happy_traveller.mixins import reCAPTCHAValidation
from django.contrib.auth.models import User
from happy_traveller.mixins import *
from google_APIs.controller import API_Controller
from WebApp_core.controller import Controller
from django.conf import settings
from .forms import *


@login_required(login_url='signin')
def account(request):
    api = API_Controller(request=request)
    controller = Controller(request=request)
    location = get_current_location()['loc']
    api.samples = 3
    context = {}
    place_id_more_info = controller.get_tag_more_info(tag='more_info')
    
    if place_id_more_info['status'] == 200:
        result = api.place(place_id=place_id_more_info['result'])
        return render(request, 'WebApp_core/place_details.html', context={"result":result})

    hotel = api.near_by_places(location=location, type='hotel')

    cafe = api.near_by_places(location=location, type='cafe')

    bar = api.near_by_places(location=location, type='bar')

    context = {
        "hotel": hotel,
        "cafe": cafe,
        "bar": bar
        }
    return render(request, 'register/account.html', context=context)


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
        print(form.errors)

        if form.is_valid():
            result = reCAPTCHAValidation(data)

            if result['success']:
                form.save()
                user = authenticate(request, username=data['username'], password=data['password2'])

                if user is not None:
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    profile = Profile.objects.get(user=request.user)
                    profile.captcha_score = result['score']
                    profile.save()
                    return redirect(success_url)
    else:
        form = SingupForm()
    return render(request, template_name, {"form":form, "public_key":settings.RECAPTCHA_PUBLIC_KEY})



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
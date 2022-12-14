from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from happy_traveller.mixins import reCAPTCHAValidation
from django.contrib.auth.models import User
from happy_traveller.mixins import *
from google_APIs.controller import API_Controller
from django.conf import settings
from .forms import *


@login_required(login_url='signin')
def account(request):
    api = API_Controller()
    samples = 3
    context = {}
    place_id_more_info = request.GET.get('more_info')
    
    if place_id_more_info:
        result = api.get_place(place_id=(place_id_more_info))
        if 'photos' in result:
            temp = api.get_photos_from_place(photos=result['photos'][:samples])
        else:
            temp = []
        result['photos_names'] = temp
        return render(request, 'WebApp_core/place_details.html', context={"result":result})

    places = api.get_near_by_places(type='hotel')[:samples]
    hotel = api.get_photo_from_all_places(places)

    places = api.get_near_by_places(type='cafe')[:samples]
    cafe = api.get_photo_from_all_places(places)

    places = api.get_near_by_places(type='bar')[:samples]
    bar = api.get_photo_from_all_places(places)

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
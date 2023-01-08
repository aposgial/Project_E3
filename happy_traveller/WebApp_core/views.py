from django.shortcuts import render, redirect
from django.urls import reverse
from google_APIs.controller import GoogleMapsController
from flickr_API.controller import FlickrController
from WebApp_core.controller import Controller
from happy_traveller.mixins import get_random_country

# Create your views here.
def home(request):
    controller = Controller(request=request)
    country = get_random_country()
    #controller.flickr_controller.most_famous_place()
    print(country)
    controller.google_maps_controller.samples = 1
    context = {}

    if request.method == 'GET':
        search = controller.get_tag_search(tag='search')
        place_id_more_info = controller.get_tag_more_info(tag='more_info')
        #option = request.GET.get('flexRadioDefault')

        if search['status'] == 200:
            result = controller.google_maps_controller.find_place(text_input=search['result'])
            return render(request, 'WebApp_core/place_details.html', context={"result":result['results']})

        if place_id_more_info['status'] == 200:
            result = controller.google_maps_controller.place(place_id=place_id_more_info['result'])
            return render(request, 'WebApp_core/place_details.html', context={"result":result['results']})

    query = country + ' tourist_attraction'
    tourist_attraction = controller.google_maps_controller.places(query=query)
    
    query = country + ' museum'
    museum = controller.google_maps_controller.places(query=query)
    
    query = country + ' park'
    park = controller.google_maps_controller.places(query=query)

    context = {
        "country": country,
        "tourist_attraction": tourist_attraction,
        "museum": museum,
        "park": park
    }

    #zip(*(iter(park),)*group)
    return render(request, 'WebApp_core/home.html', context=context)


def place_details(request):
    return render(request, 'WebApp_core/place_details.html')


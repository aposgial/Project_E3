from django.shortcuts import render, redirect
from django.urls import reverse
from google_APIs.controller import API_Controller
from happy_traveller.mixins import get_random_country

# Create your views here.
def home(request):
    api = API_Controller()
    country = get_random_country()
    samples = 3
    context = {}

    if request.method == 'GET':
        search = request.GET.get('search')
        place_id_more_info = request.GET.get('more_info')
        #option = request.GET.get('flexRadioDefault')

        if search:
            result = api.get_place_by_search(search_input=search)
            if 'photos' in result:
                temp = api.get_photos_from_place(photos=result['photos'][:samples])
            else:
                temp = []
            result['photos_names'] = temp
            return render(request, 'WebApp_core/place_details.html', context={"result":result})

        if place_id_more_info:
            result = api.get_place(place_id=(place_id_more_info))
            if 'photos' in result:
                temp = api.get_photos_from_place(photos=result['photos'][:samples])
            else:
                temp = []
            result['photos_names'] = temp
            return render(request, 'WebApp_core/place_details.html', context={"result":result})

    places = api.get_places(type='tourist_attraction', country=country)[:samples]
    tourist_attraction = api.get_photo_from_all_places(places)
    
    places = api.get_places(type='museum', country=country)[:samples]
    museum = api.get_photo_from_all_places(places)
    
    places = api.get_places(type='park', country=country)[:samples]
    park = api.get_photo_from_all_places(places)

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


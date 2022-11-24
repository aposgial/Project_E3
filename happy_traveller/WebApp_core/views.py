from django.shortcuts import render
from google_APIs.controller import API_Controller

# Create your views here.
def home(request):
    api = API_Controller()
    samples = 3
    context = {}

    places = api.get_random_country_places(type='tourist_attraction')[:samples]
    tourist_attraction = api.get_photo_from_all_places(places)
    
    museum = api.get_random_country_places(type='museum')[:samples]
    park = api.get_random_country_places(type='park')[:samples]


    if request.method == 'GET':
        search = request.GET.get('search')
        option = request.GET.get('flexRadioDefault')

        if search and option:
            api.search_location = search
            infos = api.get_places_info()
            results = []
            
            for info in infos:
                if info['category'] == 'city' and option == 'city':
                    results.append(info)
                    

                elif info['category'] == 'place' and option == 'place':
                    results.append(info)
                    
            context = {
                "search":True,
                "results":results}
        else:
            context = {
                "search":False}

    context['tourist_attraction'] = tourist_attraction
    context['museum'] = museum
    context['park'] = park
    
    return render(request, 'WebApp_core/home.html', context=context)

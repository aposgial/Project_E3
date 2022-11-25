from django.shortcuts import render
from google_APIs.controller import API_Controller
from happy_traveller.mixins import get_random_country

# Create your views here.
def home(request):
    api = API_Controller()
    samples = 6
    context = {}

    country = get_random_country()
    places = api.get_places(type='tourist_attraction', country=country)
    tourist_attraction = api.get_photo_from_all_places(places)
    
    #museum = api.get_random_country_places(type='museum')[:samples]
    #park = api.get_random_country_places(type='park')[:samples]


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
    
    if len(tourist_attraction) % 2 == 0:
        #temp = zip(*(iter(tourist_attraction),)*group)
        pass
    else:
        pass

    context = {
        "country": country,
        "tourist_attraction": tourist_attraction
    }

    #context['museum'] = zip(*(iter(museum),)*group)
    #context['park'] = zip(*(iter(park),)*group)
    
    return render(request, 'WebApp_core/home.html', context=context)

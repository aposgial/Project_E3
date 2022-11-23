from django.shortcuts import render
from google_APIs.controller import API_Controller

# Create your views here.
def home(request):
    api = API_Controller()

    tourist_attraction = api.get_random_country_places(type='tourist_attraction')[:5]
    museum = api.get_random_country_places(type='museum')[:5]
    park = api.get_random_country_places(type='park')[:5]

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
                "search":False,
                "tourist_attraction":tourist_attraction,
                "museum":museum,
                "park":park}

    context['tourist_attraction'] = tourist_attraction,
    context['museum']
    context['park']

    return render(request, 'WebApp_core/home.html', context=context)

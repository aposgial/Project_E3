from django.shortcuts import render
from google_APIs.controller import API_Controller

# Create your views here.
def home(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        option = request.GET.get('flexRadioDefault')

        if search and option:
            api = API_Controller(search_location=search)
            infos = api.get_places_info()
            results = []
            #api.get_photos(infos[0]['place_id'])
            for info in infos:
                if info['category'] == 'city' and option == 'city':
                    results.append(info)

                elif info['category'] == 'place' and option == 'place':
                    results.append(info)
                    
            context = {
                "search":True,
                "results":results}
        else:
            context = {"search":False}
        
    return render(request, 'WebApp_core/home.html', context=context)

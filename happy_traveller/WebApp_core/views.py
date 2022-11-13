from django.shortcuts import render
from google_APIs.controller import API_Controller

# Create your views here.
def home(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        option = request.GET.get('flexRadioDefault')
        print(option)
        print(search)
        if search:
            #api = API_Controller(search_location=search)
            #api.get_photos()
            context = {
                "search":True,
                #"result": api.get_place_info()
                }
        else:
            context = {"search":False}
        
    return render(request, 'WebApp_core/home.html', context=context)

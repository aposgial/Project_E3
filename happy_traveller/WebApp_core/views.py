from django.shortcuts import render
from google_APIs.controller import API_Controller

# Create your views here.
def home(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        print(search)
        if search:
            api = API_Controller(search_location=search)
            context = {
                "search":True,
                "result": api.get_place_info
                }
        else:
            context = {"search_resualt":False}
        
    return render(request, 'WebApp_core/home.html', context=context)

def login(request):
    return render(request, 'WebApp_core/sign_in.html')

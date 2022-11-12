from django.shortcuts import render
from google_APIs.views import get_photos

# Create your views here.
def home(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        print(search)
        if search:
            get_photos(location_name=search)
            context = {"search_resualt":True}
        else:
            context = {"search_resualt":False}
        
    return render(request, 'WebApp_core/home.html', context=context)

def login(request):
    return render(request, 'WebApp_core/sign_in.html')

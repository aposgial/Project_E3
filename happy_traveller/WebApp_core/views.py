from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'WebApp_core/home.html')

def map(request):
    return render(request, 'WebApp_core/map.html')

def maptest(request):
    return render(request, 'WebApp_core/maptest.html')



def login2(request):
    return render(request, 'WebApp_core/login2.html')
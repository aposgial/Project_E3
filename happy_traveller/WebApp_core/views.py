from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'WebApp_core/home.html')

def login(request):
    return render(request, 'WebApp_core/sign_in.html')

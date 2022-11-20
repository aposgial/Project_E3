from django.shortcuts import render
from .controller import API_Controller
from happy_traveller.mixins import *
# Create your views here.
def data(request):
    temp = get_current_location()
    print(temp['loc'])
    return render(request, 'google_APIs/data.html', context=temp)
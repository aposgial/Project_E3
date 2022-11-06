from django.shortcuts import render

# Create your views here.
def api_data(request):
    data:dict = {}


    text = 'ggsdfgskjvnejfkv'
    number = 1234



    data['mytext'] = text
    data['mynumber'] = number



    





    return render(request, 'google_APIs/data.html', context=data)
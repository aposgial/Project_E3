from django.shortcuts import render
import googlemaps
from datetime import datetime

# Create your views here.
def api_data(request):
    data:dict = {}



    gmaps = googlemaps.Client(key='AIzaSyCXkHhw6U2tB0iTRVlorOn4Dr0XQu8f2FI',
     client_id=None,
     client_secret=None,
     timeout=None, connect_timeout=None, read_timeout=None, retry_timeout=60, requests_kwargs=None, queries_per_second=50, channel=None, retry_over_query_limit=True)

    # Geocoding an address
    geocode_result:list = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    # Look up an address with reverse geocoding
    #reverse_geocode_result = gmaps.directions(alternatives=True,mode='driving', departure_time =50)

    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                        "Parramatta, NSW",
                                        mode="transit",
                                        departure_time=now)
    #print(geocode_result)
    data['geocode_rs'] = directions_result
    data['directions_rs'] = directions_result

    places_result = gmaps.places_neardy(location='33.8670522,151.1957362',radius =40000, open_now =False, type ='cafe')

    my_place_id = places_result['result'][0]['place id']
    print(my_place_id)
    
    



    return render(request, 'google_APIs/data.html', context=data)
from django.shortcuts import render
import googlemaps
from datetime import datetime

# Create your views here.
def api_data(request):
    data:dict = {}



    googlemaps.Client(key='AIzaSyCXkHhw6U2tB0iTRVlorOn4Dr0XQu8f2FI',
     client_id=None,
     client_secret=None,
     timeout=None, connect_timeout=None, read_timeout=None, retry_timeout=60, requests_kwargs=None, queries_per_second=50, channel=None, retry_over_query_limit=True)

    # Geocoding an address
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                        "Parramatta, NSW",
                                        mode="transit",
                                        departure_time=now)


    data['geocode_rs'] = geocode_result
    data['reverse_geocode_rs'] = reverse_geocode_result
    data['directions_rs'] = directions_result 
    



    return render(request, 'google_APIs/data.html', context=data)
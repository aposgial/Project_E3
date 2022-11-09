
{"installed":{
    "client_id":"175710163255-4i1a4be4d2aifdei8t0d9brvdosuff1o.apps.googleusercontent.com",
    "project_id":"neon-gist-367020",
    "auth_uri":"https://accounts.google.com/o/oauth2/auth",
    "token_uri":"https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
    "client_secret":"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",
    "redirect_uris":["http://localhost"]
    }
}

from django.shortcuts import render
import googlemaps
from datetime import datetime

# Create your views here.
def api_data(request):
    data:dict = {}



    gmaps = googlemaps.Client(key='AIzaSyCXkHhw6U2tB0iTRVlorOn4Dr0XQu8f2FI',
    client_id="175710163255-4i1a4be4d2aifdei8t0d9brvdosuff1o.apps.googleusercontent.com",
    client_secret="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",
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

    result = gmaps.find_place(input=['Greece'], input_type='textquery')['candidates'][0]


    photos:list = gmaps.place(place_id=result['place_id'], fields=['photo'])['result']['photos']
   
    for index, photo in enumerate(photos):
        finall_photo = gmaps.places_photo(photo_reference=photo['photo_reference'], max_width=400, max_height=400)
        f = open('photos/photo{}.jpg'.format(index), 'wb')
        for chunk in finall_photo:
            if chunk:
             f.write(chunk)
    f.close()

    return render(request, 'google_APIs/data.html', context=data)
from django.shortcuts import render
import googlemaps
from datetime import datetime

# Create your views here.
def api_data(request):
    data:dict = {}



    gmaps = googlemaps.Client(key='AIzaSyCXkHhw6U2tB0iTRVlorOn4Dr0XQu8f2FI')
    
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
    
    data['geocode_rs'] = directions_result

    location_name = 'Serres' 

    result = gmaps.find_place(input= location_name, input_type='textquery')['candidates'][0]

    photos:list = gmaps.place(place_id=result['place_id'], fields=['photo'])['result']['photos']
   
    for index, photo in enumerate(photos):
        finall_photo = gmaps.places_photo(photo_reference=photo['photo_reference'], max_width=400, max_height=400)
        f = open('google_APIs/photos/photo{}.jpg'.format(index), 'wb')
        for chunk in finall_photo:
            if chunk:
             f.write(chunk)
    f.close()

    try:
        places_name = gmaps.place(place_id=result['place_id'],fields=['name'])['result']['name']
        data['places_namee'] = places_name
    except:
        data['places_namee'] = ''
    try:
        places_open_close = gmaps.places(query = location_name )['results'][0]['opening_hours']['open_now']
        data['places_open_Hours'] = places_open_close
    except:
        data['places_open_Hours'] = None
    
    places_Address = gmaps.places(query = location_name )['results'][0]['formatted_address']
    data['places_addres'] = places_Address

    try:
        places_rate = gmaps.places(query = location_name )['results'][0]['rating']
        data['places_rating'] = places_rate
    except:
        data['places_rating'] = 0

    places_location_lat = gmaps.places(query = location_name )['results'][0]['geometry']['location']['lat']
    data['places_loclat'] = places_location_lat
    places_location_lng = gmaps.places(query = location_name )['results'][0]['geometry']['location']['lng']
    data['places_loclng'] = places_location_lng

    places_info = gmaps.places(query = location_name )
    data['places_inf'] = places_info
   
    
 
 
 
    return render(request, 'google_APIs/data.html', context=data)

    
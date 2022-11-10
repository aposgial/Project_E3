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
    

    result = gmaps.find_place(input=['Athens'], input_type='textquery')['candidates'][0]

    photos:list = gmaps.place(place_id=result['place_id'], fields=['photo'])['result']['photos']
   
    for index, photo in enumerate(photos):
        finall_photo = gmaps.places_photo(photo_reference=photo['photo_reference'], max_width=400, max_height=400)
        f = open('google_APIs/photos/photo{}.jpg'.format(index), 'wb')
        for chunk in finall_photo:
            if chunk:
             f.write(chunk)
    f.close()


    places_name = gmaps.place(place_id=result['place_id'],fields=['name'])['result']
    data['places_nm'] = places_name

    
    location_name = 'Athens'
    places_info = gmaps.places(query = location_name )
    data['places_inf'] = places_info

    find_place_rs = gmaps.find_place(input=['Athens'], input_type='textquery')
    data['places_fp'] = find_place_rs

    
 
 
 
    return render(request, 'google_APIs/data.html', context=data)

    
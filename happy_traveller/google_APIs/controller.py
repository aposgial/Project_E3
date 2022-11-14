from django.conf import settings
import googlemaps
import random

class API_Controller():
    def __init__(self, search_location:str='') -> None:
        self.client = googlemaps.Client(key=settings.GOOGLE_API_KEY)
        self.search_location = search_location


    def get_photo(self, photo_reference:str) -> str:
        try:
            photo_name = 'photo{}.jpg'.format(str(random.randint(0,1000)))

            finall_photo = self.client.places_photo(photo_reference=photo_reference, max_width=400, max_height=400)
            print('ok..')
            with open('static/photos/{}'.format(photo_name), 'wb') as f:
                for chunk in finall_photo:
                    if chunk:
                        f.write(chunk)
            return photo_name
        except Exception as e:
            print(e)
            return ''

    def get_photos(self, place_id:str):
        photos_names = []
        try:
            photos:list = self.client.place(place_id=place_id, fields=['photo'])['result']['photos']
        
            for photo in photos:
                photo_name = 'photo{}.jpg'.format(str(random.randint(0,10000)))
                finall_photo = self.client.places_photo(photo_reference=photo['photo_reference'], max_width=400, max_height=400)

                with open('static/photos/{}'.format(photo_name), 'wb') as f:
                    for chunk in finall_photo:
                        if chunk:
                            photos_names.append(photo_name)
                            f.write(chunk)

            return photos_names
        except Exception as e:
            print(e)
            return []

    
    def get_places_info(self):
        data = []
        results:list = self.client.places(query=self.search_location)['results']
        try:
            for result in results:
                if result['name']:
                    name = result['name']

                if 'opening_hours' in result:
                    open_now = result['opening_hours']['open_now']
                else:
                    open_now = None

                if 'formatted_address' in result:
                    formatted_address = result['formatted_address']

                if 'rating' in result:
                    rating = result['rating']
                    category = 'place'
                else:
                    category = 'city'

                if 'geometry' in result:
                    lat = result['geometry']['location']['lat']
                    lng = result['geometry']['location']['lng']

                if 'place_id' in result:
                    place_id = result['place_id']

                if 'photos' in result:
                    print('ref ok..')
                    photo_name = self.get_photo(str(result['photos'][0]['photo_reference']))

                if category == 'place':
                    data.append({
                        "category":category,
                        "name": name,
                        "open_now":open_now,
                        "formatted_address":formatted_address,
                        "rating":rating,
                        "loclat":lat,
                        "loclng":lng,
                        "place_id":place_id,
                        "photo_name":photo_name
                    })
                elif category == 'city':
                    data.append({
                        "category":category,
                        "name": name,
                        "formatted_address":formatted_address,
                        "loclat":lat,
                        "loclng":lng,
                        "place_id":place_id,
                        "photo_name":photo_name
                    })
            return data
        except Exception as e:
            print(e)
            return []

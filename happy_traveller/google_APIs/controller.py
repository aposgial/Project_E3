from django.conf import settings
import googlemaps

class API_Controller():
    def __init__(self, search_location:str='') -> None:
        self.client = googlemaps.Client(key=settings.GOOGLE_API_KEY)
        self.search_location = search_location


    def get_photo(self, photo_reference:str) -> list:
        try:
            photo_name = photo_reference + '.jpg'
            finall_photo = self.client.places_photo(photo_reference=photo_reference, max_width=400, max_height=400)
            
            with open('photos/{}'.format(photo_name), 'wb') as f:
                for chunk in finall_photo:
                    if chunk:
                        f.write(chunk)
            return photo_name
        except:
            return ''

    def get_photos(self, place_id:str):
        photos_names = []
        try:
            photos:list = self.client.place(place_id=place_id, fields=['photo'])['result']['photos']
        
            for photo in photos:
                photo_name = str(photo['photo_reference']) + '.jpg'
                finall_photo = self.client.places_photo(photo_reference=photo['photo_reference'], max_width=400, max_height=400)

                with open('photos/{}'.format(photo_name), 'wb') as f:
                    for chunk in finall_photo:
                        if chunk:
                            photos_names.append(photo_name)
                            f.write(chunk)

            return photos_names
        except Exception as e:
            print(e)
            return []

    
    def get_places_info(self, option:str):
        data = []
        results:list = self.client.places(query=self.search_location)['results']
        try:
            if option == 'place':
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
                    else:
                        rating = None

                    if 'geometry' in result:
                        lat = result['geometry']['location']['lat']
                        lng = result['geometry']['location']['lng']

                    if 'place_id' in result:
                        place_id = result['place_id']

                    if 'photos' in result:
                        photo_name = self.get_photo(result['photos'][0]['photo_reference'])

                    data.append({
                        "name": name,
                        "open_now":open_now,
                        "formatted_address":formatted_address,
                        "rating":rating,
                        "loclat":lat,
                        "loclng":lng,
                        "place_id":place_id,
                        "photo_name":photo_name
                    })
                return data
            elif option == 'city':
                for result in results:
                    if result['name']:
                        name = result['name']

                    if 'formatted_address' in result:
                        formatted_address = result['formatted_address']

                    if 'geometry' in result:
                        lat = result['geometry']['location']['lat']
                        lng = result['geometry']['location']['lng']

                    if 'place_id' in result:
                        place_id = result['place_id']

                    if 'photos' in result:
                        photo_name = self.get_photo(result['photos'][0]['photo_reference'])
                    data.append({
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

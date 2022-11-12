from django.conf import settings
import googlemaps

class API_Controller():
    def __init__(self, search_location:str='') -> None:
        self.client = googlemaps.Client(key=settings.GOOGLE_API_KEY)
        self.search_location = search_location


    def _get_place_name(self) -> str:
        try:
            result = self.client.find_place(input=self.search_location, input_type='textquery')['candidates'][0]
            return self.client.place(place_id=result['place_id'],fields=['name'])['result']['name']
        except:
            return ''

    def get_photos(self):
        result = self.client.find_place(input=self.search_location, input_type='textquery')['candidates'][0]
        photos:list = self.client.place(place_id=result['place_id'], fields=['photo'])['result']['photos']
    
        for index, photo in enumerate(photos):
            finall_photo = self.client.places_photo(photo_reference=photo['photo_reference'], max_width=400, max_height=400)
            with open('static/photos/photo{}.jpg'.format(index), 'wb') as f:
                for chunk in finall_photo:
                    if chunk:
                        f.write(chunk)

    
    def get_place_info(self):
        try:
            result = self.client.places(query=self.search_location )
            return {
                "name": self._get_place_name(),
                "open_now": result['results'][0]['opening_hours']['open_now'],
                "address": result['results'][0]['formatted_address'],
                "rating": result['results'][0]['rating'],
                "loclat": result['results'][0]['geometry']['location']['lat'],
                "loclng": result['results'][0]['geometry']['location']['lng']
            }
        except:
            return {
                "name": self.get_place_info()
            }

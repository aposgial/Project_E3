from django.conf import settings
import googlemaps

class GoogleMaosApi:
    def __init__(self) -> None:
        self.client = googlemaps.Client(key=settings.GOOGLE_API_KEY)


    def get_place(self, place_id:str='') -> dict:
        if place_id:
            try:
                response = self.client.place(place_id=place_id)
                if response['status'] == 'OK':
                    return response['result']
                else:
                    return {}
            except:
                return {}
        else:
            return {}

    def get_places(self, query:str='') -> list:
        if query:
            response = self.client.places(query=query)
            if response['status'] == 'OK':
                return response['results']
            else:
                return []
        else:
            return []

    def get_place_id_by_text(self, text_input:str='') -> str:
        try:
            response =  self.client.find_place(input=text_input, input_type='textquery')['candidates'][0]['place_id']
            return response
        except:
            return ''

    def get_near_by_places(self, location:str, radius=1000, type:str='') -> list:
        try:
            response = self.client.places_nearby(location=location, radius=radius, type=type)
            if response['status'] == 'OK':
                return response['results']
            else:
                return []
        except:
            return []

    def get_photo(self, photo_reference:str) -> str:
        if photo_reference:
            try:
                response = self.client.places_photo(photo_reference=photo_reference, max_width=400, max_height=400)
                return response
            except:
                return ''
        else:
            return ''

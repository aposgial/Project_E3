from happy_traveller.mixins import *
from services import GoogleMapsApi
import random, time


class API_Controller(GoogleMapsApi):
    def __init__(self, search_location:str='') -> None:
        self.search_location = search_location


    def find_place_by_text(self, text_input:str=''):
        service = self.get_place_id_by_text(text_input)

        if service['status'] == 200:
            return service['results']
        elif service['status'] == 204:
            return
        elif service['status'] == 404:
            return
        elif service['status'] == 400:
            return
        elif service['status'] == 429:
            return
        elif service['status'] == 403:
            return
        elif service['status'] == 417:
            return
        elif service['status'] == 11001:
            return
        else:
            return

    def place(self, place_id:str=''):
        service = self.get_place(place_id)

        if service['status'] == 200:
            return service['results']
        elif service['status'] == 204:
            return
        elif service['status'] == 404:
            return
        elif service['status'] == 400:
            return
        elif service['status'] == 429:
            return
        elif service['status'] == 403:
            return
        elif service['status'] == 417:
            return
        elif service['status'] == 11001:
            return
        else:
            return
        

    def places(self, query:str=''):
        service = self.get_places(query)

        if service['status'] == 200:
            return service['results']
        elif service['status'] == 204:
            return
        elif service['status'] == 404:
            return
        elif service['status'] == 400:
            return
        elif service['status'] == 429:
            return
        elif service['status'] == 403:
            return
        elif service['status'] == 417:
            return
        elif service['status'] == 11001:
            return
        else:
            return

    def near_by_places(self, location:str, radius=1000, type:str=''):
        service = self.get_near_by_places(location, radius, type)

        if service['status'] == 200:
            return service['results']
        elif service['status'] == 204:
            return
        elif service['status'] == 404:
            return
        elif service['status'] == 400:
            return
        elif service['status'] == 429:
            return
        elif service['status'] == 403:
            return
        elif service['status'] == 417:
            return
        elif service['status'] == 11001:
            return
        else:
            return

    def photo(self, photo_reference:str):
        service = self.get_photo(photo_reference)

        if service['status'] == 200:
            return service['results']
        elif service['status'] == 204:
            return
        elif service['status'] == 404:
            return
        elif service['status'] == 400:
            return
        elif service['status'] == 429:
            return
        elif service['status'] == 403:
            return
        elif service['status'] == 417:
            return
        elif service['status'] == 11001:
            return
        else:
            return


    def download_photo(self, photo_reference:str) -> str:
        try:
            photo_name = 'photo{}.jpg'.format(str(random.randint(0,1000)))

            finall_photo = self.client.places_photo(photo_reference=photo_reference, max_width=400, max_height=400)
            with open('static/photos/{}'.format(photo_name), 'wb') as f:
                for chunk in finall_photo:
                    if chunk:
                        f.write(chunk)
            return photo_name
        except Exception as e:
            print(e)
            return ''

    def download_photo_from_all_places(self, places:list) -> list:
        for index, place in enumerate(places):
            try:
                photo = place['photos'][0]['photo_reference']
                photo_name = self.get_photo(photo_reference=photo)
                if photo_name:
                    place['photo_name'] = photo_name
            except KeyError:
                places.pop(index)
        return places
            

    def download_photos_from_place(self, photos:list) -> list:
        photos_names = []
        for photo in photos:
            photo_name = self.get_photo(photo_reference=photo['photo_reference'])
            if photo_name:
                photos_names.append(photo_name)
        return photos_names



    def get_place_by_search(self, search_input:str='') -> dict:
        if search_input:
            try:
                place_id = self.client.find_place(input=search_input, input_type='textquery')['candidates'][0]['place_id']
                return self.get_place(place_id=place_id)
            except:
                return {}
        else:
            return {}

        
    def get_random_country_places(self, type:str='') -> list:
        country = get_random_country()
        if country:
            return self.get_places(type=type, country=country)
        else:
            return []
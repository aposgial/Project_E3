from happy_traveller.mixins import *
from google_APIs.services import GoogleMapsApi
from google_APIs.messages import GoogleMapsMessages
from concurrent import futures


class GoogleMapsController(GoogleMapsApi, GoogleMapsMessages):
    def __init__(self, request) -> None:
        super().__init__()
        self.request = request
        self.samples = 10
        self.photo_width = 400
        self.photo_height = 400


    def _place_id_by_text(self, text_input:str='') -> dict:
        service = self.get_place_id_by_text(text_input)

        if service['status'] == 200:
            service['message'] = self.success()
            return service
        elif service['status'] == 204:
            service['message'] = self.no_results_for_place()
            return service
        elif service['status'] == 404:
            service['message'] = self.no_found()
            return service
        elif service['status'] == 400:
            service['message'] = self.invalid_request()
            return service
        elif service['status'] == 429:
            service['message'] = self.over_query_limit()
            return service
        elif service['status'] == 403:
            service['message'] = self.request_denied()
            return service
        elif service['status'] == 417:
            service['message'] = self.unknown_error()
            return service
        elif service['status'] == 11001:
            service['message'] = self.no_internet_connection()
            return service
        else:
            return

    def _place(self, place_id:str='') -> dict:
        service = self.get_place(place_id)

        if service['status'] == 200:
            service['message'] = self.success()
            return service
        elif service['status'] == 204:
            service['message'] = self.no_results()
            return service
        elif service['status'] == 404:
            service['message'] = self.no_found()
            return service
        elif service['status'] == 400:
            service['message'] = self.invalid_request()
            return service
        elif service['status'] == 429:
            service['message'] = self.over_query_limit()
            return service
        elif service['status'] == 403:
            service['message'] = self.request_denied()
            return service
        elif service['status'] == 417:
            service['message'] = self.unknown_error()
            return service
        elif service['status'] == 11001:
            service['message'] = self.no_internet_connection()
            return service
        else:
            return
        
    def _places(self, query:str='') -> dict:
        service = self.get_places(query)

        if service['status'] == 200:
            service['message'] = self.success()
            return service
        elif service['status'] == 204:
            service['message'] = self.no_results()
            return service
        elif service['status'] == 404:
            service['message'] = self.no_found()
            return service
        elif service['status'] == 400:
            service['message'] = self.invalid_request()
            return service
        elif service['status'] == 429:
            service['message'] = self.over_query_limit()
            return service
        elif service['status'] == 403:
            service['message'] = self.request_denied()
            return service
        elif service['status'] == 417:
            service['message'] = self.unknown_error()
            return service
        elif service['status'] == 11001:
            service['message'] = self.no_internet_connection()
            return service
        else:
            return

    def _near_by_places(self, location:str, radius=1000, type:str='') -> dict:
        service = self.get_near_by_places(location, radius, type)

        if service['status'] == 200:
            service['message'] = self.success()
            return service
        elif service['status'] == 204:
            service['message'] = self.no_results()
            return service
        elif service['status'] == 404:
            service['message'] = self.no_found()
            return service
        elif service['status'] == 400:
            service['message'] = self.invalid_request()
            return service
        elif service['status'] == 429:
            service['message'] = self.over_query_limit()
            return service
        elif service['status'] == 403:
            service['message'] = self.request_denied()
            return service
        elif service['status'] == 417:
            service['message'] = self.unknown_error()
            return service
        elif service['status'] == 11001:
            service['message'] = self.no_internet_connection()
            return service
        else:
            return

    def _photo(self, photo_reference:str) -> dict:
        service = self.get_photo(photo_reference, width=self.photo_width, height=self.photo_height)

        if service['status'] == 200:
            service['message'] = self.success()
            return service
        elif service['status'] == 404:
            service['message'] = self.no_found()
            return service
        elif service['status'] == 400:
            service['message'] = self.invalid_request()
            return service
        elif service['status'] == 429:
            service['message'] = self.over_query_limit()
            return service
        elif service['status'] == 403:
            service['message'] = self.request_denied()
            return service
        elif service['status'] == 417:
            service['message'] = self.unknown_error()
            return service
        elif service['status'] == 11001:
            service['message'] = self.no_internet_connection()
            return service
        else:
            return


    def _download_photo(self, photo_reference:str) -> dict:
        photo:dict = self._photo(photo_reference=photo_reference)

        if photo['status'] == 200:
            photo_name = 'photo{}.jpg'.format(str(random_number()))

            with open('static/photos/{}'.format(photo_name), 'wb') as f:
                for chunk in photo['results']:
                    if chunk:
                        f.write(chunk)
                photo.update({"results":photo_name})
                return photo
        else:
            return photo

    def _download_photo_from_all_places(self, places:list) -> list:
        photos_references = []
        for index, place in enumerate(places):
            try:
                photos_references.append(place['photos'][0]['photo_reference'])
            except KeyError:
                places.pop(index)

        with futures.ThreadPoolExecutor(max_workers=10) as executor:
            photos = executor.map(self._download_photo, photos_references)

            for photo, place in zip(photos, places):
                if photo['status'] == 200:
                    place['photo_name'] = photo['results']

        return places
            
    def _download_photos_from_place(self, photos:list) -> list:
        photos_names = []
        photos_references = []

        for photo in photos:
            photos_references.append(photo['photo_reference'])

        with futures.ThreadPoolExecutor(max_workers=10) as executor:
            temp = executor.map(self._download_photo, photos_references)

            for photo in temp:
                if photo['status'] == 200:
                    photos_names.append(photo['results'])

        return photos_names


    def place(self, place_id:str='') -> dict:
        result = self._place(place_id=place_id)
        
        if result['status'] == 200 and "photos" in result['results']:
            result['results']['photos_names'] = self._download_photos_from_place(photos=result['results']['photos'])
            return result
        else:
            return result

    def places(self, query:str='') -> dict:
        result = self._places(query=query)

        if result['status'] == 200:
            temp =  self._download_photo_from_all_places(places=result['results'][:self.samples])
            result.update({"results": temp})
            return result
        else:
            return result

    def find_place(self, text_input:str='') -> dict:
        result = self._place_id_by_text(text_input=text_input)

        if result['status'] == 200:
            return self.place(place_id=result['results'])
        else:
            return result

    def near_by_places(self, location:str, radius=1000, type:str='') -> dict:
        result = self._near_by_places(location=location, radius=radius, type=type)
    
        if result['status'] == 200:
            temp =  self._download_photo_from_all_places(places=result['results'][:self.samples])
            result['results'] = temp
            return result
        else:
            return result


    def random_country_places(self, type:str='') -> dict:
        country = get_random_country()
        if country:
            query = type + ' ' + country
            return self.places(query=query)
        else:
            return {
                "status": 204,
                "message": self.no_country_found()
            }
        
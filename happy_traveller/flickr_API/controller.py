from flickr_API.services import FlickrApi
from flickr_API.messages import FlickrMessages
from happy_traveller.mixins import get_countries
<<<<<<< HEAD

class FlickrApiController(FlickrApi, FlickrMessages):
    def __init__(self, request) -> None:
        super().__init__()
        self.request = request

=======
from concurrent import futures

class FlickrController(FlickrApi, FlickrMessages):
    def __init__(self, request) -> None:
        super().__init__()
        self.request = request
        self.accuracy:int = 3
        self.threads:int = 10
>>>>>>> b21866201ba26765dcbc6538de57e96ab4f5f560

    def place_by_search(self, text_input:str=''):
        service = self.get_place_by_search(text_input)

        if service['status'] == 200:
            service['message'] = self.success()
            return service
        elif service['status'] == 204:
            service['message'] = self.no_results_for_search()
            return service
        elif service['status'] == 10:
            service.update({
                "message": self.flickr_message_error(message=service['message'])
                })
            return service
        elif service['status'] == 18:
            service.update({
                "message": self.flickr_message_warning(message=service['message'])
                })
            return service
        elif service['status'] == 105:
            service.update({
                "message": self.flickr_message_info(message=service['message'])
                })
            return service
        elif service['status'] == 106:
            service.update({
                "message": self.flickr_message_error(message=service['message'])
                })
            return service
        elif service['status'] == 111:
            service.update({
                "message": self.flickr_message_error(message=service['message'])
                })
            return service
        elif service['status'] == 112:
            service.update({
                "message": self.flickr_message_error(message=service['message'])
                })
            return service
        elif service['status'] == 114 or service['status'] == 115:
            service.update({
                "message": self.flickr_message_error(message=service['message'])
                })
            return service
        elif service['status'] == 116:
            service.update({
                "message": self.flickr_message_warning(message=service['message'])
                })
            return service

        if service['status'] == 404:
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

    
<<<<<<< HEAD
    def total_place_photos(self, text_input:str='',accuracy:int=3) -> dict:
        sum_photos:int = 0
        for loop in range(accuracy):
=======
    def total_place_photos(self, text_input:str='') -> dict:
        sum_photos:int = 0
        for _ in range(self.accuracy):
>>>>>>> b21866201ba26765dcbc6538de57e96ab4f5f560
            photos = self.place_by_search(text_input)
            if photos['status'] == 200:
                sum_photos =+ int(photos['results']['total'])
        
<<<<<<< HEAD
        return sum_photos // accuracy

    def most_famous_place(self, city:bool=False, accuracy:int=3) -> str:
        if city:
            self.place_type = 11

        places_total_photos:list = []
        countries = get_countries()[:10]
        for place in countries:
            total_photos:int = self.total_place_photos(text_input=str(place), accuracy=accuracy)
            places_total_photos.append(total_photos)
=======
        return sum_photos // self.accuracy

    def most_famous_place(self, city:bool=False) -> str:
        if city:
            self.place_type = 11

        places_total_photos = []
        countries = get_countries()[:10]
        
        with futures.ThreadPoolExecutor(max_workers=self.threads) as executor:
            temp = executor.map(self.total_place_photos, countries)

            for place_total_photos in temp:
                places_total_photos.append(place_total_photos)
>>>>>>> b21866201ba26765dcbc6538de57e96ab4f5f560

        index:int = places_total_photos.index(max(places_total_photos))
        return countries[index]
        
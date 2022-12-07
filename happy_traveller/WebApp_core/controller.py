from google_APIs.controller import GoogleMapsController
from flickr_API.controller import FlickrController
from WebApp_core.messages import Messeges

class Controller(Messeges):
    def __init__(self, request) -> None:
        super().__init__(request)
        self.google_maps_controller = GoogleMapsController(request=request)
        self.flickr_controller = FlickrController(request=request)

    
    def get_tag_search(self, tag:str) -> dict:
        value:str = self.request.GET.get(tag)

        if value:
            return {
                "status": 200,
                "result": value,
                "message": self.success_search()
            }
        else:
            return {
                "status": 204,
                "message": self.empty_search()
            }

    def get_tag_more_info(self, tag:str) -> dict:
        value:str = self.request.GET.get(tag)

        if value:
            return {
                "status": 200,
                "result": value,
                "message": self.success_more_info()
            }
        else:
            return {
                "status": 204,
                "message": self.empty_more_info()
            }
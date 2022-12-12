from google_APIs.controller import GoogleMapsController
from flickr_API.controller import FlickrController
from WebApp_core.controller import Controller as Contr
from register.messages import Messeges

class Controller(Messeges):
    def __init__(self, request) -> None:
        super().__init__(request)
        self.google_maps_controller = GoogleMapsController(request=request)
        self.flickr_controller = FlickrController(request=request)
        self.webapp_core_controller = Contr(request=request)

    
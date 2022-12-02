from google_APIs.controller import GoogleMapsApi
from register.messages import Messeges

class Controller(GoogleMapsApi, Messeges):
    def __init__(self, request) -> None:
        super().__init__(request)

    
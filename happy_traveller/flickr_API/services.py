from django.conf import settings
import requests

class FlickrApi:
    def __init__(self) -> None:
        self.key = settings.FLICKR_API_KEY
        self.base_url = 'https://www.flickr.com/services/rest/?'
        self.accuracy = 3

    def get_place_by_search(self, text_input:str=''):
        url = "{base_url}method=flickr.photos.search&api_key={key}&text={text}&accuracy={accuracy}&content_type=1&format=json&nojsoncallback=1".format(
            base_url = self.base_url,
            key = self.key,
            text = text_input,
            accuracy = self.accuracy
        )

        response =  requests.get(url=url).json()
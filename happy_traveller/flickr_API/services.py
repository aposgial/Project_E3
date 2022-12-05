from django.conf import settings
from flickr_API.exceptions import *
import requests

class FlickrApi:
    def __init__(self) -> None:
        self.key = settings.FLICKR_API_KEY
        self.base_url = 'https://www.flickr.com/services/rest/?'
        self.accuracy = 3
        self.expect = requests.exceptions


    def get_place_by_search(self, text_input:str=''):
        url = "{base_url}method=flickr.photos.search&api_key={key}&text={text}&accuracy={accuracy}&content_type=1&format=json&nojsoncallback=1".format(
            base_url = self.base_url,
            key = self.key,
            text = text_input,
            accuracy = self.accuracy
        )

        try:
            response =  requests.get(url=url).json()

            if response['stat'] == 'ok':
                return {
                    "status": 200,
                    "results": response['photos']
                }
            elif response['stat'] == 'ok' and response['total'] == 0:
                return {
                    "status": 204,
                }
            else:
                return {
                    "status": response['code'],
                    "message": response['message']
                }
        except self.expect.HTTPError as err:
            return {
                "status": err.response.status_code
            }
        except self.expect.ConnectionError:
            return {
                "status": 11001
            }
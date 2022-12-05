from flickr_API.services import FlickrApi
from flickr_API.messages import FlickrMessages

class FlickrApiController(FlickrApi, FlickrMessages):
    def __init__(self, request) -> None:
        super().__init__()
        self.request = request


    def _place_by_search(self, text_input:str=''):
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
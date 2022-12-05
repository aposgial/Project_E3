from django.contrib import messages

class FlickrMessages:
    def __init__(self, request) -> None:
        self.request = request
    

    def flickr_message_error(self, message:str=''):
        return messages.error(self.request, message=message)

    def flickr_message_warning(self, message:str=''):
        return messages.warning(self.request, message=message)

    def flickr_message_info(self, message:str=''):
        return messages.info(self.request, message=message)
    

    def success(self):
        return messages.info(self.request, message='The data retrieved successfully')

    def no_results_for_search(self):
        return messages.info(self.request, message='No results for this search.')

    def no_found(self):
        return messages.error(self.request, message='Page not found.')

    def invalid_request(self):
        return messages.error(self.request, message='Your request is invalid.')

    def over_query_limit(self):
        return messages.warning(self.request, message='You have exceeded the request limits.')

    def request_denied(self):
        return messages.warning(self.request, message='You are unauthorized and do not have access rights to this content.')

    def unknown_error(self):
        return messages.error(self.request, message='Something gone wrong.')

    def no_internet_connection(self):
        return messages.error(self.request, message='No internet connection.')
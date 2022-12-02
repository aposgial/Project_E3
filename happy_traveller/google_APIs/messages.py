from django.contrib import messages

class GoogleMapsMessages(messages):
    def __init__(self, request) -> None:
        super().__init__()
        self.message = messages
        self.request = request

    def success(self):
        return self.message.success(self.request, message='The request succeeded.')

    def no_results_for_search(self):
        return self.message.info(self.request, message='No results for this search.')

    def no_results(self):
        return self.message.info(self.request, message='No results for this place.')

    def no_found(self):
        return self.message.error(self.request, message='Page not found.')

    def invalid_request(self):
        return self.message.error(self.request, message='Your request is invalid.')

    def over_query_limit(self):
        return self.message.warning(self.request, message='You have exceeded the request limits.')

    def request_denied(self):
        return self.message.warning(self.request, message='You are unauthorized and do not have access rights to this content.')

    def unknown_error(self):
        return self.message.error(self.request, message='Something gone wrong.')

    def no_internet_connection(self):
        return self.message.error(self.request, message='No internet connection.')

    def no_country_found(self):
        return self.message.error(self.request, message='Can not pick a random country.')
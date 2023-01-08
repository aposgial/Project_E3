from django.contrib import messages

class GoogleMapsMessages:
    def __init__(self, request) -> None:
        self.request = request

    def success(self):
        return messages.success(self.request, message='The request succeeded.')

    def no_results_for_place(self):
        return messages.info(self.request, message='No results for this search.')

    def no_results(self):
        return messages.info(self.request, message='No results for this place.')

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

    def no_country_found(self):
        return messages.error(self.request, message='Can not pick a random country.')
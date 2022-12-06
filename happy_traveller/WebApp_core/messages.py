from django.contrib import messages


class Messeges:
    def __init__(self, request) -> None:
        self.request = request


    def success_search(self):
        return messages.success(self.request, message='The search succeeded.')

    def empty_search(self):
        return messages.warning(self.request, message='Please fulfill the search area.')

    def success_more_info(self):
        return messages.success(self.request, message='More details to come.')

    def empty_more_info(self):
        return messages.warning(self.request, message='this place has not more details.')
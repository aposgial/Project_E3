from django.contrib import messages


class Messeges(messages):
    def __init__(self, request) -> None:
        super().__init__()
        self.request = request
        self.message = messages


    def success_search(self):
        return self.message.success(self.request, message='The search succeeded.')

    def empty_search(self):
        return self.message.warning(self.request, message='Please fulfill the search area.')

    def success_more_info(self):
        return self.message.success(self.request, message='More details to come.')

    def empty_more_info(self):
        return self.message.warning(self.request, message='this place has not more details.')
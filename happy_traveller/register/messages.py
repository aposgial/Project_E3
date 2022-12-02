from django.contrib import messages


class Messeges(messages):
    def __init__(self, request) -> None:
        super().__init__()
        self.request = request
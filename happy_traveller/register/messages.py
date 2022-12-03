from django.contrib import messages


class Messeges:
    def __init__(self, request) -> None:
        self.request = request
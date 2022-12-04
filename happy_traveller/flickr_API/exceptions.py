class ApiError(Exception):
    def __init__(self, *args: object, status:int=None, message:str=None) -> None:
        super().__init__(*args)
        self.status = status
        self.message = message

    def __str__(self) -> str:
        return super().__str__() + "{status} {message}".format(status=self.status, message=self.message)


class ApiNotAvailableError(ApiError):
    pass

class IllogicalArgumentsError(ApiError):
    pass

class ServiceUnavailableError(ApiError):
    pass

class OperationError(ApiError):
    pass

class FormatError(ApiError):
    pass

class MethodError(ApiError):
    pass

class ParseError(ApiError):
    pass

class UrlError(ApiError):
    pass

class NoResultsError(Exception):
    pass
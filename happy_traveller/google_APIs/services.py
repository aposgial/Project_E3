from django.conf import settings
import googlemaps

class GoogleMapsApi:
    def __init__(self) -> None:
        self.client = googlemaps.Client(key=settings.GOOGLE_API_KEY)
        self.expect = googlemaps.exceptions


    def get_place(self, place_id:str='') -> dict:
            try:
                response = self.client.place(place_id=place_id)

                if response['status'] == 'OK':
                    return {
                        "status": 200,
                        "results": response['results']
                        }
                else:
                    return {
                        "status": 204
                        }

            except self.expect.ApiError as err:
                if err.status == "NOT_FOUND":
                    return {
                        "status": 404
                        }
                elif err.status == "INVALID_REQUEST":
                    return {
                        "status": 400
                        }
                elif err.status == "OVER_QUERY_LIMIT":
                    return {
                        "status": 429
                        }
                elif err.status == "REQUEST_DENIED":
                    return {
                        "status": 403
                        }
                elif err.status == "UNKNOWN_ERROR":
                    return {
                        "status": 417
                        }     
            except self.expect.HTTPError as status_code:
                return {
                    "status":status_code
                    } 
            except self.expect.TransportError:
                return {
                    "status": 11001
                    }

    def get_places(self, query:str='') -> dict:
        try:
            response = self.client.places(query=query)

            if response['status'] == 'OK':
                return {
                    "status": 200,
                    "results": response['results']
                    }
            else:
                return {
                    "status": 204
                    }

        except self.expect.ApiError as err:
            if err.status == "NOT_FOUND":
                return {
                    "status": 404
                    }
            elif err.status == "INVALID_REQUEST":
                return {
                    "status": 400
                    }
            elif err.status == "OVER_QUERY_LIMIT":
                return {
                    "status": 429
                    }
            elif err.status == "REQUEST_DENIED":
                return {
                    "status": 403
                    }
            elif err.status == "UNKNOWN_ERROR":
                return {
                    "status": 417
                    }     
        except self.expect.HTTPError as status_code:
            return {
                "status":status_code
                } 
        except self.expect.TransportError:
            return {
                "status": 11001
                }

    def get_place_id_by_text(self, text_input:str='') -> dict:
        try:
            response =  self.client.find_place(input=text_input, input_type='textquery')

            if response['status'] == 'OK':
                return {
                    "status": 200,
                    "results": response['candidates'][0]
                    }
            else:
                return {
                    "status": 204
                    }

        except self.expect.ApiError as err:
            if err.status == "NOT_FOUND":
                return {
                    "status": 404
                    }
            elif err.status == "INVALID_REQUEST":
                return {
                    "status": 400
                    }
            elif err.status == "OVER_QUERY_LIMIT":
                return {
                    "status": 429
                    }
            elif err.status == "REQUEST_DENIED":
                return {
                    "status": 403
                    }
            elif err.status == "UNKNOWN_ERROR":
                return {
                    "status": 417
                    }     
        except self.expect.HTTPError as status_code:
            return {
                "status":status_code
                } 
        except self.expect.TransportError:
            return {
                "status": 11001
                }

    def get_near_by_places(self, location:str, radius=1000, type:str='') -> dict:
        try:
            response = self.client.places_nearby(location=location, radius=radius, type=type)

            if response['status'] == 'OK':
                return {
                    "status": 200,
                    "results": response['results']
                    }
            else:
                return {
                    "status": 204
                    }

        except self.expect.ApiError as err:
            if err.status == "NOT_FOUND":
                return {
                    "status": 404
                    }
            elif err.status == "INVALID_REQUEST":
                return {
                    "status": 400
                    }
            elif err.status == "OVER_QUERY_LIMIT":
                return {
                    "status": 429
                    }
            elif err.status == "REQUEST_DENIED":
                return {
                    "status": 403
                    }
            elif err.status == "UNKNOWN_ERROR":
                return {
                    "status": 417
                    }     
        except self.expect.HTTPError as status_code:
            return {
                "status":status_code
                } 
        except self.expect.TransportError:
            return {
                "status": 11001
                }

    def get_photo(self, photo_reference:str) -> dict:
        try:
            response = self.client.places_photo(photo_reference=photo_reference, max_width=400, max_height=400)
            return {
                    "status": 200,
                    "results": response
                    }
        except self.expect.ApiError as err:
            if err.status == "NOT_FOUND":
                return {
                    "status": 404
                    }
            elif err.status == "INVALID_REQUEST":
                return {
                    "status": 400
                    }
            elif err.status == "OVER_QUERY_LIMIT":
                return {
                    "status": 429
                    }
            elif err.status == "REQUEST_DENIED":
                return {
                    "status": 403
                    }
            elif err.status == "UNKNOWN_ERROR":
                return {
                    "status": 417
                    }     
        except self.expect.HTTPError as status_code:
            return {
                "status":status_code
                } 
        except self.expect.TransportError:
            return {
                "status": 11001
                }


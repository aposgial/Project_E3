from django.test import TestCase
from google_APIs.controller import GoogleMapsController
import unittest
from django.http import HttpRequest

# Create your tests here.

class Test_ApiController(unittest.TestCase):
    def setUp(self):
        self.request = HttpRequest()
        self.GooglemapsControllers= GoogleMapsController(request=self.request)
        self.samples = 3
        self.text_input = "rome"
        self.place_id = "ChIJu46S-ZZhLxMROG5lkwZ3D7k"
        self.query = "museum"
        self.location="40.6436,22.9309"
        self.radius=1000
        self.type="tourist_attraction"
        self.photo_reference="AW30NDwcZUMKbiQ_oQr8udiITYN0sbJpEbxG-bCsk5np5w0BpCCtelvb_7HmRXL4jZVWcxZJNCln7ZhWUIyhUAsGeWOdYVyGSSke8all9IDXwFqD6wzKL_VCSW9Z-7FW6LKefe0uqhDd0jP76kugHhcUxcLorTmAf6MWTJ9a75vuHzgrZrc4"
        self.width =400
        self.height=400
        self.places= [
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Piazza del Colosseo, 1, 00184 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.8902102,
                        "lng": 12.4922309
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.89147139999999,
                            "lng": 12.49511675
                        },
                        "southwest": {
                            "lat": 41.8875602,
                            "lng": 12.48862095
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
                "icon_background_color": "#13B5C7",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
                "name": "Colosseum",
                "opening_hours": {
                    "open_now": True
                },
                "photos": [
                    {
                        "height": 1987,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/113437494756768394691\">Ovidiu Burca</a>"
                        ],
                        "photo_reference": "AW30NDxr502LFFzRXfB3IVL9hhKCjQsyNTFX_NhQH4vj4uh75eNhdqslfCEy9x-Cyj5T0Hx7UMiG5PDgRB7qrYl-rMEabHi-Ji02nTa_4uYpAqdcbjyK8KA_a4lBWTn1xBe2xd6aE7kPrq7r_EflQS3ZCpTEnbEg4fe3ahsp-qmLamedm1YJ",
                        "width": 3000
                    }
                ],
                "place_id": "ChIJrRMgU7ZhLxMRxAOFkC7I8Sg",
                "plus_code": {
                    "compound_code": "VFRR+3V Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJVFRR+3V"
                },
                "rating": 4.7,
                "reference": "ChIJrRMgU7ZhLxMRxAOFkC7I8Sg",
                "types": [
                    "tourist_attraction",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 322125
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Via della Salara Vecchia, 5/6, 00186 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.8924623,
                        "lng": 12.485325
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.89653735,
                            "lng": 12.4945579
                        },
                        "southwest": {
                            "lat": 41.88770114999999,
                            "lng": 12.4801987
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/museum-71.png",
                "icon_background_color": "#13B5C7",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/museum_pinlet",
                "name": "Roman Forum",
                "opening_hours": {
                    "open_now": True
                },
                "photos": [
                    {
                        "height": 2268,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/115242435534319781640\">Jean-pierre Binet</a>"
                        ],
                        "photo_reference": "AW30NDwcRcUD8ePptmuJfTQmePUB0RTzvY5d4iehGZdzQQfpJc_WpI6uHRlATLWT_44wyeQpIE_Nnw0dyxKZ9jeY5jx2nNCvs13jnbGWWEDONX3ShIvU2-4eB59K9R0aASYdnPa5yU-Mp6pwLl5R7vEMCrKJfoKrcCyhBHQx4vkocFyIhE25",
                        "width": 4032
                    }
                ],
                "place_id": "ChIJ782pg7NhLxMR5n3swAdAkfo",
                "plus_code": {
                    "compound_code": "VFRP+X4 Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJVFRP+X4"
                },
                "rating": 4.7,
                "reference": "ChIJ782pg7NhLxMR5n3swAdAkfo",
                "types": [
                    "museum",
                    "tourist_attraction",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 113397
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Piazza del Popolo, 00187 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.9107038,
                        "lng": 12.4763579
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.91201807989272,
                            "lng": 12.47788957989272
                        },
                        "southwest": {
                            "lat": 41.90931842010728,
                            "lng": 12.47518992010728
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
                "icon_background_color": "#7B9EB0",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
                "name": "Piazza del Popolo",
                "opening_hours": {
                    "open_now": True
                },
                "photos": [
                    {
                        "height": 6936,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/104557188475014626148\">marco di cristoforo</a>"
                        ],
                        "photo_reference": "AW30NDwCW1P2oYSbfNJinU-q78nTH7FQEkPqPfpqiC6Sw58IzulLczE-i8jAfbApZoCLIPOX_Gm54fiXqlEphBslTfDJpsrxfRBUzI3fla5X1PbEwMbAoRwymbdyKBYwSUe-j4KSkWbLw5qwxT9p21AsrMnU_gU3693QiZufiyVp6qkfY6Za",
                        "width": 9248
                    }
                ],
                "place_id": "ChIJhxbo5fhgLxMRUEPO_f-f7kM",
                "plus_code": {
                    "compound_code": "WF6G+7G Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJWF6G+7G"
                },
                "rating": 4.6,
                "reference": "ChIJhxbo5fhgLxMRUEPO_f-f7kM",
                "types": [
                    "tourist_attraction",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 87634
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Piazza Navona, 00186 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.8991633,
                        "lng": 12.4730742
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.90178655,
                            "lng": 12.4746868
                        },
                        "southwest": {
                            "lat": 41.89645714999998,
                            "lng": 12.47142799999999
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
                "icon_background_color": "#7B9EB0",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
                "name": "Piazza Navona",
                "opening_hours": {
                    "open_now": True
                },
                "photos": [
                    {
                        "height": 3375,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/102888276412420232045\">luis vidilla</a>"
                        ],
                        "photo_reference": "AW30NDy7nWjBP8vdd_WkJcYZLlzNfjQFJ68LeaVJFxrje_EIi-BrQTTeL_UiV6R7xDkXnhBlbcO-AfbAbaxr9pTQaol6oDn-syvM2kB6r6Id1axN22GuVRc3i2BT5wuxZhOUXVUA8YXOioImtM6hNzDFKCVMsx9Q0_86o8dhTINUKAW1qNIX",
                        "width": 5400
                    }
                ],
                "place_id": "ChIJPRydwYNgLxMRSjOCLlYkV6M",
                "plus_code": {
                    "compound_code": "VFXF+M6 Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJVFXF+M6"
                },
                "rating": 4.7,
                "reference": "ChIJPRydwYNgLxMRSjOCLlYkV6M",
                "types": [
                    "tourist_attraction",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 154216
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Piazza di Spagna, 00187 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.90599,
                        "lng": 12.482775
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.90743154999998,
                            "lng": 12.48419145
                        },
                        "southwest": {
                            "lat": 41.90406175000001,
                            "lng": 12.48060765
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/museum-71.png",
                "icon_background_color": "#7B9EB0",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/monument_pinlet",
                "name": "Spanish Steps",
                "opening_hours": {},
                "photos": [
                    {
                        "height": 3024,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/113337142574254463220\">Bobby</a>"
                        ],
                        "photo_reference": "AW30NDwOoTiyp7gUKUz-qASZA9bH8s__5LdBfNpORG3xChMXOBf6qORG-RuwDpYVJazdHFwDj8kGtd4hCVdnQNI-bt_4EELoGGK4UD3ErAFEX4siJBTmU1RMHybVceooDWMM0kdXeVVNNK4VGS4Bc5anNVy-oFfk-kqU1fIHLV9m0yikvcMy",
                        "width": 4032
                    }
                ],
                "place_id": "ChIJda54FlRgLxMRD2muipfUwH8",
                "plus_code": {
                    "compound_code": "WF4M+94 Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJWF4M+94"
                },
                "rating": 4.5,
                "reference": "ChIJda54FlRgLxMRD2muipfUwH8",
                "types": [
                    "tourist_attraction",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 55508
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Piazza di Trevi, 00187 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.9009325,
                        "lng": 12.483313
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.90227397989272,
                            "lng": 12.48449002989272
                        },
                        "southwest": {
                            "lat": 41.89957432010727,
                            "lng": 12.48179037010728
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/park-71.png",
                "icon_background_color": "#4DB546",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/tree_pinlet",
                "name": "Trevi Fountain",
                "opening_hours": {
                    "open_now": True
                },
                "photos": [
                    {
                        "height": 588,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/100248671337702850036\">Sanjay Sharma</a>"
                        ],
                        "photo_reference": "AW30NDxBH_F0caJmdue0A3Ho8uxL_gxfDKpe4vOGl6b88sZhuQn4DvmANoRXePB_uQPfCXXVpZJ7XsBydbd9EWb55HW3cAlDij0ss8g4CHl-l7Y454b_JLQrdj1LyGuSAu5SAozr-PWMyXehgYIiE7IlFYpAlcIRmbhwCVupzB5D2HJ-tMlF",
                        "width": 1024
                    }
                ],
                "place_id": "ChIJ1UCDJ1NgLxMRtrsCzOHxdvY",
                "plus_code": {
                    "compound_code": "WF2M+98 Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJWF2M+98"
                },
                "rating": 4.8,
                "reference": "ChIJ1UCDJ1NgLxMRtrsCzOHxdvY",
                "types": [
                    "tourist_attraction",
                    "park",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 336386
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Piazza della Rotonda, 00186 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.8986108,
                        "lng": 12.4768729
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.90011307989273,
                            "lng": 12.47817452989272
                        },
                        "southwest": {
                            "lat": 41.89741342010728,
                            "lng": 12.47547487010728
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/museum-71.png",
                "icon_background_color": "#7B9EB0",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/monument_pinlet",
                "name": "Pantheon",
                "opening_hours": {
                    "open_now": True
                },
                "photos": [
                    {
                        "height": 700,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/114858402738038040071\">A Google User</a>"
                        ],
                        "photo_reference": "AW30NDztzRLIe4U-LLcbVmCzUXyd153DiKt5peES4wzGHZwJl2zETMs5WgqSuKHLsz7ue7bECpVidcn2HUj7sJ3k42lRQ3LfNlX6hkB7duGyEozqYoZ11dhZGVSNBPtopkEWVWwxeu6V69F5VR7ihG7SlG-eeq54JkjkMai8lnx1EZAu7s8v",
                        "width": 1050
                    }
                ],
                "place_id": "ChIJqUCGZ09gLxMRLM42IPpl0co",
                "plus_code": {
                    "compound_code": "VFXG+CP Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJVFXG+CP"
                },
                "rating": 4.8,
                "reference": "ChIJqUCGZ09gLxMRLM42IPpl0co",
                "types": [
                    "tourist_attraction",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 185002
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Piazza Navona, 00186 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.8998083,
                        "lng": 12.473027
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.90116382989272,
                            "lng": 12.47398422989272
                        },
                        "southwest": {
                            "lat": 41.89846417010728,
                            "lng": 12.47128457010728
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
                "icon_background_color": "#13B5C7",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
                "name": "Neptune Fountain",
                "opening_hours": {
                    "open_now": True
                },
                "photos": [
                    {
                        "height": 2717,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/110250919992315497958\">Gunther H.G. Geick</a>"
                        ],
                        "photo_reference": "AW30NDwd8R_Rj9NEPnUh2VAlt1RVcEmVKkdr-62CP-SuA70zU1q6O5KYdsVT6CsCyaDd0qwC-H8pkpbGqegUmk3d1v52mVSqs41vsIDw_M0J1HzTwWyxyeRUfP0v8Ii0xOeHdpXatg3aX1qJXpc1Hmj8IFeRTinLXgRmXEgT0xp2rfyCO6Wc",
                        "width": 3618
                    }
                ],
                "place_id": "ChIJT8CVIAdhLxMR4_YveMMvc2Q",
                "plus_code": {
                    "compound_code": "VFXF+W6 Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJVFXF+W6"
                },
                "rating": 4.7,
                "reference": "ChIJT8CVIAdhLxMR4_YveMMvc2Q",
                "types": [
                    "tourist_attraction",
                    "park",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 1446
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Lungotevere Castello, 50, 00193 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.9030632,
                        "lng": 12.466276
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.90415182989272,
                            "lng": 12.4701709
                        },
                        "southwest": {
                            "lat": 41.90145217010727,
                            "lng": 12.4623737
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
                "icon_background_color": "#13B5C7",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
                "name": "Castel Sant'Angelo",
                "opening_hours": {
                    "open_now": True
                },
                "photos": [
                    {
                        "height": 620,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/110765636305693516808\">A Google User</a>"
                        ],
                        "photo_reference": "AW30NDzOisQqwsjL5PlWav0OaPUvkGjNSYJ9WXJkCl0jk6sOGtAcFjvZIibw6jbQe5nN4DWzNdkxEOLihyvKW_4uSsrLGTWCINIbXhDUevIfkbmHkxLcYf-w12EWViCYyJBtq2M88piBSeWNj6ojlMBRcYFk_aIrg_0sbzNiFi4e-RQf86rR",
                        "width": 1024
                    }
                ],
                "place_id": "ChIJ0aTnEYeKJRMRiUF95xwRbDY",
                "plus_code": {
                    "compound_code": "WF38+6G Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJWF38+6G"
                },
                "rating": 4.7,
                "reference": "ChIJ0aTnEYeKJRMRiUF95xwRbDY",
                "types": [
                    "tourist_attraction",
                    "museum",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 70257
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Piazza del Campidoglio, 1, 00186 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.8929428,
                        "lng": 12.4825577
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.89470697989272,
                            "lng": 12.48373667989272
                        },
                        "southwest": {
                            "lat": 41.89200732010728,
                            "lng": 12.48103702010728
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/museum-71.png",
                "icon_background_color": "#13B5C7",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/museum_pinlet",
                "name": "Capitoline Museums",
                "opening_hours": {},
                "photos": [
                    {
                        "height": 4624,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/101377606892890388956\">mat-109@hotmail.com</a>"
                        ],
                        "photo_reference": "AW30NDy_z2MdMl91LLGQ2SycKWzNLhDOs2aYq6kDS6dECRvfFxxQ2G6jlI7Htxzb043q5qzdj5WioxgkAL6cqVUCZ8feygm7pkTHgCKRqu-o1pQvIP4sZ2WuuLkUsUyO-T63mbLQo0NSCYdVYo0tXpXPODqWnzHjG_HJEmAWV88cCVgFNhgm",
                        "width": 3472
                    }
                ],
                "place_id": "ChIJ8-wGeU9gLxMR--zJtnpGod4",
                "plus_code": {
                    "compound_code": "VFVM+52 Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJVFVM+52"
                },
                "rating": 4.7,
                "reference": "ChIJ8-wGeU9gLxMR--zJtnpGod4",
                "types": [
                    "tourist_attraction",
                    "museum",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 12890
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Piazza di Spagna, 00187 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.9056978,
                        "lng": 12.482327
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.907484,
                            "lng": 12.48368872989272
                        },
                        "southwest": {
                            "lat": 41.90404519999998,
                            "lng": 12.48098907010728
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
                "icon_background_color": "#7B9EB0",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
                "name": "Piazza di Spagna",
                "opening_hours": {},
                "photos": [
                    {
                        "height": 9024,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/113271026936428610370\">Vincenzo Arcieri</a>"
                        ],
                        "photo_reference": "AW30NDxnz21YRe26ci_pYkJmfm3FGid0cPHFKrGR7EAOcoFuNeLZZAw3K3SxmP9Di7mCGBLzhB5EydfIh9VDxDc2J8tPsmwkXUrwCFY9GUNzedQDqZr_D5A_QUKc4uVCl-EPnQKz2O8eTBMZP0UvDUuKlxe0mXPgtQy4InlFWmuKVygo2I5o",
                        "width": 12032
                    }
                ],
                "place_id": "ChIJ4_TEG1VgLxMROFkd29jWdug",
                "plus_code": {
                    "compound_code": "WF4J+7W Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJWF4J+7W"
                },
                "rating": 4.7,
                "reference": "ChIJ4_TEG1VgLxMROFkd29jWdug",
                "types": [
                    "tourist_attraction",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 110684
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Viale delle Terme di Caracalla, 00153 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.8790382,
                        "lng": 12.4924394
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.88200579999999,
                            "lng": 12.4970026
                        },
                        "southwest": {
                            "lat": 41.878049,
                            "lng": 12.489967
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
                "icon_background_color": "#13B5C7",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
                "name": "Baths of Caracalla",
                "photos": [
                    {
                        "height": 4048,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/102272790181136800074\">Carlos Ch\u00e1vez</a>"
                        ],
                        "photo_reference": "AW30NDxBx2rkArqCHFwPPhr35RCzYuo2Dnz2PAHqMfVLQyHkOS_zDq_S1xfI4ts1XB71JDrJcO70RNpdDPf-pYl5n-IrA4ZZ-Z0xiVxPoK5PxGI485q4zTr7I3FZPIQpLEYgosGIDHl9rtY3KPD24gA5gOHc4IK4WjGFbCILu8dG-YdVpbYp",
                        "width": 3036
                    }
                ],
                "place_id": "ChIJ1YU-M85hLxMR3Jhb6gZAK2o",
                "plus_code": {
                    "compound_code": "VFHR+JX Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJVFHR+JX"
                },
                "rating": 4.6,
                "reference": "ChIJ1YU-M85hLxMR3Jhb6gZAK2o",
                "types": [
                    "tourist_attraction",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 17740
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Piazzale Scipione Borghese, 5, 00197 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.9142103,
                        "lng": 12.4921442
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.91848494999999,
                            "lng": 12.49605165
                        },
                        "southwest": {
                            "lat": 41.91174835,
                            "lng": 12.48467505
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/museum-71.png",
                "icon_background_color": "#13B5C7",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/museum_pinlet",
                "name": "Borghese Gallery and Museum",
                "opening_hours": {
                    "open_now": True
                },
                "photos": [
                    {
                        "height": 9000,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/103487176514047438874\">Marwan Dessouki</a>"
                        ],
                        "photo_reference": "AW30NDwdWbClJlxwStEORlTYAnZRD2C3hcqxPn7f73R_v368keEVu-IJzuiR-PMenpUcB5poOpb80qDuGiWk_-qGvvNrUljF0il0orGMIaAQe99P9OF-BmTE-TYbf5o_Cb7OMQKZ7phr36LePcbHEsgCCzh5DdEzaPz07vGZuhM7m9t-6lI0",
                        "width": 12000
                    }
                ],
                "place_id": "ChIJq-bXVgRhLxMRv3vgOXaktBs",
                "plus_code": {
                    "compound_code": "WF7R+MV Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJWF7R+MV"
                },
                "rating": 4.6,
                "reference": "ChIJq-bXVgRhLxMRv3vgOXaktBs",
                "types": [
                    "tourist_attraction",
                    "museum",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 18039
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Piazza Venezia, 00186 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.8945976,
                        "lng": 12.4831269
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.89648309999999,
                            "lng": 12.485187
                        },
                        "southwest": {
                            "lat": 41.89305350000001,
                            "lng": 12.4816242
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
                "icon_background_color": "#7B9EB0",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
                "name": "Altar of the Fatherland",
                "opening_hours": {},
                "photos": [
                    {
                        "height": 3024,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/100985733278855539084\">Alek Karpoff</a>"
                        ],
                        "photo_reference": "AW30NDxU7XN43rfnWEeMlgO7N62hBMEMdGy9WxHu8cmTac8xxfLJc8W4ssm1BsuGhDNO4l9Rib8BHXrXQLIKOgjSiQsFbJrKdrN8SVKoTejiLzj2VujIfkVpdL_U94izhRKR98U8WWnXPXvyD6PEfuzJ3Kgsh3ustDSvhn6NH_53c3a5lekJ",
                        "width": 4032
                    }
                ],
                "place_id": "ChIJ412AG01gLxMR4T-4pwdIFSE",
                "plus_code": {
                    "compound_code": "VFVM+R7 Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJVFVM+R7"
                },
                "rating": 4.8,
                "reference": "ChIJ412AG01gLxMR4T-4pwdIFSE",
                "types": [
                    "tourist_attraction",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 47802
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Campo de' Fiori, 00186 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.8957407,
                        "lng": 12.4718483
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.89684977989273,
                            "lng": 12.47292837989272
                        },
                        "southwest": {
                            "lat": 41.89415012010728,
                            "lng": 12.47022872010728
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
                "icon_background_color": "#13B5C7",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
                "name": "Campo de' Fiori",
                "opening_hours": {
                    "open_now": True
                },
                "photos": [
                    {
                        "height": 428,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/103177555847675660842\">Roberto Vitaloni</a>"
                        ],
                        "photo_reference": "AW30NDy4Ku8NUhQmVlU8Q4NovPUO1ydTJqgM4r4K9C4QliNwT5XnWLxVZmQBQ8Wo3Tv7YKIjJ8VZqs1ABiYk7DUG4u3N-CZlKzd4JHNXV_jEu92CNDRKukoEUa_4OwZKGIVQpjcRiYt6i9i79mhshf8nKYV4S7lhrUsWcMpXpUopP0WCfy-F",
                        "width": 640
                    }
                ],
                "place_id": "ChIJfc8DqVVgLxMRxPIIp3z8CBg",
                "plus_code": {
                    "compound_code": "VFWC+7P Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJVFWC+7P"
                },
                "rating": 4.4,
                "reference": "ChIJfc8DqVVgLxMRxPIIp3z8CBg",
                "types": [
                    "tourist_attraction",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 49899
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "P.za di Santa Maria Maggiore, 00100 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.89759859999999,
                        "lng": 12.4984084
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.89872112989271,
                            "lng": 12.50032837989272
                        },
                        "southwest": {
                            "lat": 41.89602147010727,
                            "lng": 12.49762872010728
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/worship_general-71.png",
                "icon_background_color": "#7B9EB0",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/worship_christian_pinlet",
                "name": "Basilica Papale di Santa Maria Maggiore",
                "photos": [
                    {
                        "height": 2252,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/108451329392194131529\">Elena Hristova</a>"
                        ],
                        "photo_reference": "AW30NDyrJnsIWEW3jAYYKeNZRqr9g6P-QE6KhKkFvV68oq769AZ_yx82kh_10H00uwLDr3apUWamg4Fm_Idpxu9CiwSLaijj8pNQp7WNp69axlb6PMn0MKXUk35ld70P-x_qkXepkpiAg_HlA2b4iv4oXTT6bQmmrz_Ya-jpbzF2lyaFQfoJ",
                        "width": 4000
                    }
                ],
                "place_id": "ChIJ1zB926RhLxMRejWMj_tUs_c",
                "plus_code": {
                    "compound_code": "VFXX+29 Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJVFXX+29"
                },
                "rating": 4.8,
                "reference": "ChIJ1zB926RhLxMRejWMj_tUs_c",
                "types": [
                    "tourist_attraction",
                    "church",
                    "place_of_worship",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 26931
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Foro Traiano, 85, 00186 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.8960502,
                        "lng": 12.484071
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.89730807989272,
                            "lng": 12.48564097989272
                        },
                        "southwest": {
                            "lat": 41.89460842010728,
                            "lng": 12.48294132010728
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
                "icon_background_color": "#13B5C7",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
                "name": "Le Domus Romane di Palazzo Valentini",
                "opening_hours": {
                    "open_now": False
                },
                "photos": [
                    {
                        "height": 3024,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/115869602625590323499\">Philippe Gabriel</a>"
                        ],
                        "photo_reference": "AW30NDwCG21IL9OyRvp84F1MAGxrWHM7C19jR4smfemVlrMnyNMhr9wOM3ZDJLXvbNXBUrzs3QbmXDZfDtPWVobSF2wfbpmCBcdJLw6OtxbkOYhaPVifrjOgezA7wCgAuxZX0Aj6UBeWlIPlmRt2MnG6HZdld2cxWPQ0KsI7ldhGTfuyVH9t",
                        "width": 4032
                    }
                ],
                "place_id": "ChIJr2C1NU1gLxMRAQ8Cfk1debk",
                "plus_code": {
                    "compound_code": "VFWM+CJ Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJVFWM+CJ"
                },
                "rating": 4.7,
                "reference": "ChIJr2C1NU1gLxMRAQ8Cfk1debk",
                "types": [
                    "tourist_attraction",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 1307
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Piazza del Campidoglio, 00186 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.8933592,
                        "lng": 12.4828018
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.89460562989272,
                            "lng": 12.48421872989272
                        },
                        "southwest": {
                            "lat": 41.89190597010728,
                            "lng": 12.48151907010728
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
                "icon_background_color": "#13B5C7",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
                "name": "Campidoglio",
                "opening_hours": {},
                "photos": [
                    {
                        "height": 3000,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/115696991637340209912\">Martin Scharinger</a>"
                        ],
                        "photo_reference": "AW30NDxhY92cz0_BqIwNaDSgGpdAxZ-hz6De-_DUYCvLFwF3VaCJSkVJqWlVmDEr5vACSFR65cuLN8Qrn0EqAeXEMj3fyb5Vt7QL38vNMBsa8RPPLq9vpfO_s0xzdh4unhb8vkhZVMUC2leVMm797WRZ-6h9wyRApOLloUlctjBlYw4UwNOi",
                        "width": 4000
                    }
                ],
                "place_id": "ChIJOclom0xgLxMRURy9OLL7Hg4",
                "plus_code": {
                    "compound_code": "VFVM+84 Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJVFVM+84"
                },
                "rating": 4.7,
                "reference": "ChIJOclom0xgLxMRURy9OLL7Hg4",
                "types": [
                    "tourist_attraction",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 19330
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "P.za di S. Giovanni in Laterano, 4, 00184 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.8858811,
                        "lng": 12.505673
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.88756042989272,
                            "lng": 12.5103292
                        },
                        "southwest": {
                            "lat": 41.88486077010727,
                            "lng": 12.5018088
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/worship_general-71.png",
                "icon_background_color": "#7B9EB0",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/worship_christian_pinlet",
                "name": "Basilica di San Giovanni in Laterano",
                "photos": [
                    {
                        "height": 3000,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/113162537286602979534\">\u0141ukasz Zieli\u0144ski</a>"
                        ],
                        "photo_reference": "AW30NDxb-jNjsVTSxsyUBSGdsoUU340kUknIXcMJ_zighxlw9Mu4lHq85rM3NDPMCi-xyCXIzHObAch3xtql438grYGw-pJ3dr9QLVZsfbfFmFuBG8xQd4kUDPudmMVFeVWAsKYyf9Fkxpkubod2TzHFdhDxXEdayLUQ9Cye2cN5kOsxSjLC",
                        "width": 4000
                    }
                ],
                "place_id": "ChIJc6vKf79hLxMR-JBUkZ--MAE",
                "plus_code": {
                    "compound_code": "VGP4+97 Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJVGP4+97"
                },
                "rating": 4.8,
                "reference": "ChIJc6vKf79hLxMR-JBUkZ--MAE",
                "types": [
                    "tourist_attraction",
                    "church",
                    "place_of_worship",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 20956
            },
            {
                "business_status": "OPERATIONAL",
                "formatted_address": "Piazzale Napoleone I, 00197 Roma RM, Italy",
                "geometry": {
                    "location": {
                        "lat": 41.9128873,
                        "lng": 12.4852085
                    },
                    "viewport": {
                        "northeast": {
                            "lat": 41.9200584,
                            "lng": 12.50134455
                        },
                        "southwest": {
                            "lat": 41.906272,
                            "lng": 12.46863755
                        }
                    }
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/park-71.png",
                "icon_background_color": "#4DB546",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/tree_pinlet",
                "name": "Villa Borghese",
                "opening_hours": {},
                "photos": [
                    {
                        "height": 9000,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/101604462021960204365\">Baby Vicky</a>"
                        ],
                        "photo_reference": "AW30NDxkjDKV64hsVk081hCCO7saFegCpwfb8ZvEbxDMiKtgMpWjlnQ-7PB7JOWach3y6O5NoMstA7PValPtWC37ZR_meZRmeLvWZN-ImBmScq5OXqLfiIRJvCWqlzjtiLlqfVOrX4ATlT3fFd4StjcZx6hGEpDlzNK-MwnV68UafIaQdRk6",
                        "width": 12000
                    }
                ],
                "place_id": "ChIJj1M8HQJhLxMRRI6D_z18Pes",
                "plus_code": {
                    "compound_code": "WF7P+53 Rome, Metropolitan City of Rome, Italy",
                    "global_code": "8FHJWF7P+53"
                },
                "rating": 4.6,
                "reference": "ChIJj1M8HQJhLxMRRI6D_z18Pes",
                "types": [
                    "park",
                    "tourist_attraction",
                    "point_of_interest",
                    "establishment"
                ],
                "user_ratings_total": 68009
            }
        ]
        self.photo=[
                    {
                        "height": 1987,
                        "html_attributions": [
                            "<a href=\"https://maps.google.com/maps/contrib/113437494756768394691\">Ovidiu Burca</a>"
                        ],
                        "photo_reference": "AW30NDxr502LFFzRXfB3IVL9hhKCjQsyNTFX_NhQH4vj4uh75eNhdqslfCEy9x-Cyj5T0Hx7UMiG5PDgRB7qrYl-rMEabHi-Ji02nTa_4uYpAqdcbjyK8KA_a4lBWTn1xBe2xd6aE7kPrq7r_EflQS3ZCpTEnbEg4fe3ahsp-qmLamedm1YJ",
                        "width": 3000
                    }
                ]
        self.place={'address_components': [{'long_name': 'Rome', 'short_name': 'Rome', 'types': ['locality', 'political']}, {'long_name': 'Rome', 'short_name': 'Rome', 'types': ['administrative_area_level_3', 'political']}, {'long_name': 'Metropolitan City of Rome', 'short_name': 'RM', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Lazio', 'short_name': 'Lazio', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'Italy', 'short_name': 'IT', 'types': ['country', 'political']}], 'adr_address': '<span class="locality">Rome</span>, <span class="region">Metropolitan City of Rome</span>, <span class="country-name">Italy</span>', 'formatted_address': 'Rome, Metropolitan City of Rome, Italy', 'geometry': {'location': {'lat': 41.9027835, 'lng': 12.4963655}, 'viewport': {'northeast': {'lat': 42.05054624539585, 'lng': 12.73028878823088}, 'southwest': {'lat': 41.76959604595655, 'lng': 12.34170704408109}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/geocode-71.png', 'icon_background_color': '#7B9EB0', 'icon_mask_base_uri': 'https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet', 'name': 'Rome', 'photos': [{'height': 3024, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/115152600256821602962">le fab</a>'], 'photo_reference': 'ARywPAKWC-3H995pO5OdUjNFbfWIc8U9uxQuMWIYbDdUVHu5-gHLg-o_RJtllk8WBo6ENrAhtWBD0bbw6ouuEiviBc0Bv8fB76gDmimpDWnezxWVCOgzj64pRi7on7mfYzrB6s2RCE01ejHEJd1ykoBaZ_r8arCqYbQ-2j9P8cCelcv-U4Ik', 'width': 4032}, {'height': 4624, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/100972198880877396077">Günter Kellermann</a>'], 'photo_reference': 'ARywPAKMZcjQ7jqHnNxcHMF4T5lFrh4unps7sjIxDSlVmsy8UZs6N1or90mB4Kdya0fHGx0MuRF6fkkBLaLip8ssrjU2rs47CpEsGD7bbi2PqAqjOVnd5Por12nEIQ0NCOqMie4nKIT7TrAWqeMlCLtmjFuO1Y9_R5qgBlngJsTwCEW5BIWf', 'width': 2604}, {'height': 9000, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/105067273240844869805">Ана Павловић</a>'], 'photo_reference': 'ARywPALMMVP0A0SfumuyxVkkhua2s6bXjCJVfgpULvhMRRPDlE_jgDzSyIwi-YXHtsxxrCbRTmSlveT-E9TMgUN6SJK1HeExEsiU-Cmt5JHJ10kiz9vQqOa5ZQhgK8Z5tWMqIolzI79hg1UC3qdsgkv7dhMJWk9faBTmxkTPrPcjtDkXMoEJ', 'width': 12000}, {'height': 2988, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/101736542057834696103">simon green</a>'], 'photo_reference': 'ARywPAJfGq6gy1JuUvCltfcypxmqQpCPPZO6l2g9y55OH4YlSm1LWnnE_peSdNYEGOD8L4C5cFpK9qv0X0ElTompLwGYHUIGY-ysqiIrktBrhZBZgL3z6tJqER_tFu1zqHzO8eIHeckfSytWJb4HTpHMwuaRMNP0jsVsOjMidR6j_vLLDcfZ', 'width': 5312}, {'height': 2240, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/100606586420303808152">GIANCARLO GENTILE</a>'], 'photo_reference': 'ARywPAL_a5iGuZIngKno90AGijymc5Uql2BTHqzeyQvia6DQhzb1Ej6iJpoZhBT0gAHzOsg7nd0EOqBwApLbp7-d6OXd23z1DqVFo8xm_5RaFzzGmyOtgCJalmg4In8GlPZ_VGO_-BdoW1erywsTOW8IQVqEKnpe-b32_WWFHsGkvfBJdKCy', 'width': 9728}, {'height': 3000, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/110786084813951543755">julia ferro</a>'], 'photo_reference': 'ARywPAK7wgOON-F-g3Tsy9HbRKm5J5Cz5psdbWqwoTf98NEjhLsdykeBOwhnginYx2-9-N8ZuCTSrHT7CGiKSx3DV5aIu5nO8KSFRn5VK1un72mDs7JBHpoXH-ugIWGYHPizMy7bVHVB2fxEP_jeWNACK016BRuvW_4S6f00-fJcjYKEVJR8', 'width': 4000}, {'height': 3024, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/117266157076041644577">Germaine De Brouwer</a>'], 'photo_reference': 'ARywPAIwSlKF0GUYpWgORUvDF_mG-a1QsIROBtl4kVTuOL2SDhq3PBnIPMUAttwszaJuPhHz6zAdSJkcOY79GcrobFM3thQdo7ECc-1E4xtD0YGKyhNnMMjnQ-lCvx_ULvqgV01c2OsaaOmkhdeUvYAQYHHo0R5M04TRGuwqWsRb8E7UFodi', 'width': 4032}, {'height': 4032, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/100297409867339323242">Kerstin Müller</a>'], 'photo_reference': 'ARywPAIGwUyAH2zJ6U1rDISMAV5UaxxtSJqsHzEXR87RRyCT7Pusz86k2CHdRiuG40WkmS2OqO0jJumqGruJhMl0kdH4_BliIPGmoox5bAhdlx3dHJQ5w7UlA8ZKrKZ7raiULWFPBIfQ5of1Y-F9gZO48STW_pfgshRAsziNHY0eIQCUOk6C', 'width': 3024}, {'height': 1868, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/111703851884252448583">Pietro Fiscaletti</a>'], 'photo_reference': 'ARywPAJWpOOVosrD0GpZVyCD-Yc9p1_caSt8GqTPTlnfTpRYuSkl7pF1BybQQUftD-Js3LF9T06KnEK_iXmGxutXNVIKvFEpd5GPIOTrujE9mtHYnNXpCOpmTnUFjr_DS8EEeystztjLv3CR89L-h4YIJpDVD2JzzL3MzMg1IsK7b0JyC8OY', 'width': 4000}, {'height': 2252, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/101025215632302127486">Ingeborg Mjanger</a>'], 'photo_reference': 'ARywPAJ_9RIxvjs0DiMLOcQTrBsx-9gJBdUC818rqT5dUQE0oV9WiXsVdZUlBn_oH6FlYpc8iR8o1AvxK8_yS-H0n5kKya7kSsbB4-yhBUGJvGBIcQdf3Fd1SnfVAHVABQHHo2Ny19s53oxI7b9axe96dZnvCQGOF825j9GA8N_d-APndqK8', 'width': 4000}], 'place_id': 'ChIJu46S-ZZhLxMROG5lkwZ3D7k', 'reference': 'ChIJu46S-ZZhLxMROG5lkwZ3D7k', 'types': ['locality', 'political'], 'url': 'https://maps.google.com/?q=Rome,+Metropolitan+City+of+Rome,+Italy&ftid=0x132f6196f9928ebb:0xb90f770693656e38', 'utc_offset': 60, 'vicinity': 'Rome', 'website': 'http://www.comune.roma.it/'}

    def test__place_id_by_text(self):
        temp:dict = self.GooglemapsControllers._place_id_by_text(self.text_input)
        self.assertDictEqual(temp, {"status":200, "message":None, "results":self.place_id})
      
    def test__place(self):
        self.maxDiff = None
        temp:dict = self.GooglemapsControllers._place(self.place_id)
        self.assertDictEqual(temp,{"status":200, "message":None,"results":self.place})
    
    def test__places(self):
        self.assertAlmostEqual("Paris","Paris")

if __name__ == '__main__':
    unittest.main()
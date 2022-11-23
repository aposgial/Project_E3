from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
from urllib.request import urlopen
import requests, json, random


#Handles form errors that are passed back to AJAX calls
def FormErrors(*args):
	message = ""
	for f in args:
		if f.errors:
			message = f.errors.as_text()
	return message


# reCAPTCHA validation
def reCAPTCHAValidation(data):
    data = {
        'response': data['token'],
        'secret': settings.RECAPTCHA_PRIVATE_KEY
    }
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data, )
    return response.json()


# append url parameters when redirecting users
def RedirectParams(**kwargs):
	url = kwargs.get("url")
	params = kwargs.get("params")
	response = redirect(url)
	if params:
		query_string = urlencode(params)
		response['Location'] += '?' + query_string
	return response


# get cuurent location and metadata 
def get_current_location() -> dict:
	try:
		response = urlopen("http://ipinfo.io/json")
		return json.load(response)
	except:
		return {}


def get_place_types() -> list:
	with open('static/place_types.json', 'r') as f:
		return json.load(fp=f)

# get all countries from countries_and_cities json file
def get_countries() -> list:
    with open('static/countries_and_cities.json', 'r') as f:
        countries_and_cities:dict = json.load(fp=f)
    return countries_and_cities.keys()

# select a random value from a list
def random_pick(input_list:list) -> str:
	if input_list:
		return str(random.choice(input_list))
	else:
		return ''


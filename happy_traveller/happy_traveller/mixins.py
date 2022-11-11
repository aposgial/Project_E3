from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests
from django.http import JsonResponse


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
    resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data, )
    return resp.json()


# append url parameters when redirecting users
def RedirectParams(**kwargs):
	url = kwargs.get("url")
	params = kwargs.get("params")
	response = redirect(url)
	if params:
		query_string = urlencode(params)
		response['Location'] += '?' + query_string
	return response

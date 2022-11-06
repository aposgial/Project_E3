from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile

'''
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField()
    class Meta:
        model = User
        fields = ["username", "email", "firstname", "password1", "password2"]
'''

# from built-in UserCreationForm handeles user creation
class UserForm(UserCreationForm):

	first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': '*Your first name..'}))
	last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': '*Your last name..'}))
	username = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': '*Email..'}))

	password1 = forms.CharField(min_length=4, required=True, widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))
	password2 = forms.CharField(min_length=4, required=True, widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..','class':'password'}))

	#reCAPTCHA token
	token = forms.CharField(widget=forms.HiddenInput())

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'username', 'password1', 'password2', )



# from built-in AuthenticationForm handles user authentication
class AuthForm(AuthenticationForm):

	username = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': '*Email..'}))
	password = forms.CharField(min_length=4, required=True, widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))

	class Meta:
		model = User
		fields = ('username','password', )



# extends user model for userprofile
# hidden inputs renders into html
class UserProfileForm(forms.ModelForm):

	address = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	town = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	county = forms.CharField(max_length=100, required=True, widget = forms.HiddenInput())
	post_code = forms.CharField(max_length=8, required=True, widget = forms.HiddenInput())
	country = forms.CharField(max_length=40, required=True, widget = forms.HiddenInput())


	class Meta:
		model = UserProfile
		fields = ('address', 'town', 'county', 'post_code',
		 'country', )
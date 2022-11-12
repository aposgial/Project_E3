from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile


# from built-in UserCreationForm handeles user creation
class SingupForm(UserCreationForm):

	first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': '*Your first name..'}))
	last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': '*Your last name..'}))

	username = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': '*Username..'}))
	email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': '*Email..'}))

	password1 = forms.CharField(min_length=4, required=True, widget=forms.PasswordInput(attrs={'placeholder': '*Password..','class':'password'}))
	password2 = forms.CharField(min_length=4, required=True, widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password..','class':'password'}))

	#reCAPTCHA token
	token = forms.CharField(required=False,widget=forms.HiddenInput(attrs={'class':'g-recaptcha-response','id':'recaptcha'}))

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', )



# from built-in AuthenticationForm handles user authentication
class SigninForm(AuthenticationForm):

	username = forms.CharField(max_length=254, required=True, widget=forms.TextInput(attrs={'placeholder': '*Username'}))
	password = forms.CharField(min_length=4, required=True, widget=forms.PasswordInput(attrs={'placeholder': '*Password','class':'password'}))

	class Meta:
		model = User
		fields = ('username','password', )



# extends user model for userprofile
# hidden inputs renders into html
class ProfileForm(forms.ModelForm):

	address = forms.CharField(max_length=100, required=True, widget = forms.TextInput())
	town = forms.CharField(max_length=100, required=True, widget = forms.TextInput())
	county = forms.CharField(max_length=100, required=True, widget = forms.TextInput())
	post_code = forms.CharField(max_length=8, required=True, widget = forms.TextInput())
	country = forms.CharField(max_length=40, required=True, widget = forms.TextInput())


	class Meta:
		model = Profile
		fields = ('address', 'town', 'county', 'post_code', 'country', )
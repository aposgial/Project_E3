from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator


from happy_traveller.mixins import(
	AjaxFormMixin, 
	reCAPTCHAValidation,
	FormErrors,
	)


from .forms import *

result = "Error"
message = "There was an error, please try again"



# Generic FormView with our mixin to display user account page
class AccountView(TemplateView):
	template_name = "register/account.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

'''
# allow users to update their profile
def profile_view(request):
	user = request.user
	up = user.userprofile

	form = UserProfileForm(instance = up) 

	if request.is_ajax():
		form = UserProfileForm(data = request.POST, instance = up)
		if form.is_valid():
			obj = form.save()
			obj.has_profile = True
			obj.save()
			result = "Success"
			message = "Your profile has been updated"
		else:
			message = FormErrors(form)
		data = {'result': result, 'message': message}
		return JsonResponse(data)

	else:

		context = {'form': form}
		context['google_api_key'] = settings.GOOGLE_API_KEY
		context['base_country'] = settings.BASE_COUNTRY

		return render(request, 'register/profile.html', context)
'''



def signup_view(request):
    template_name = "register/sign_up.html"
    success_url = "/"

    if request.method == 'POST':
        data = request.POST
        form = SingupForm(data)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=data['username'], password=data['password2'])
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect(success_url)
    else:
        form = SingupForm()
    return render(request, template_name, {"form":form})


def signin_view(request):
    template_name = "register/sign_in.html"
    success_url = "/"

    if request.method == 'POST':
        data = request.POST
        print(data)
        form = SigninForm(data)
        if form.is_valid():
        	user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
				
                return redirect(success_url)
    else:
        form = SigninForm()
    return render(request, template_name, {"form":form})


'''
# sign-up with reCAPTURE security 
class SignUpView(FormView):
	template_name = "register/sign_up.html"
	form_class = UserForm
	success_url = "/"

	#reCAPTURE key required in context
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["recaptcha_site_key"] = settings.RECAPTCHA_PUBLIC_KEY
		return context

	#over write the mixin logic to get, check and save reCAPTURE score
	def form_valid(self, form):
		#response = super(AjaxFormMixin, self).form_valid(form)
		#response = self.form_valid(form)
		print(form.cleaned_data.get('username'))
		if self.request.is_ajax():
			
			token = form.cleaned_data.get('token')
			captcha = reCAPTCHAValidation(token)
			if captcha["success"]:
				obj = form.save()
				obj.email = obj.username
				obj.save()
				up = obj.userprofile
				up.captcha_score = float(captcha["score"])
				up.save()
				
				login(self.request, obj, backend='django.contrib.auth.backends.ModelBackend')

				#change result & message on success
				result = "Success"
				message = "Thank you for signing up"

				
			data = {'result': result, 'message': message}
			return JsonResponse(data)

		#return response



# user sign-in
class SignInView(FormView):
	template_name = "register/sign_in.html"
	form_class = AuthForm
	success_url = "/"

	def form_valid(self, form):
		#response = super(AjaxFormMixin, self).form_valid(form)	
		if self.request.is_ajax():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			#attempt to authenticate user
			user = authenticate(self.request, username=username, password=password)
			if user is not None:
				login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
				result = "Success"
				message = 'You are now logged in'
			else:
				message = FormErrors(form)
			data = {'result': result, 'message': message}
			return JsonResponse(data)
		#return response
'''


# user sign out
def sign_out(request):
	#logout(request)
	return redirect(request, "sign_out.html")
from django.urls import path
from . import views


urlpatterns = [
	
	path('account', views.AccountView.as_view(), name="account"),
	#path('profile', views.profile_view, name="profile"),
	path('signup', views.signup_view, name="signup"),
	path('signin', views.signin_view, name="signin"),
	path('signout', views.sign_out, name="signout"),
	]
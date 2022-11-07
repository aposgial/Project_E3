from django.urls import path
from . import views


urlpatterns = [
	
	path('account', views.account, name="account"),
	path('profile', views.prifile, name="profile"),
	path('signup', views.sign_up, name="signup"),
	path('signin', views.sign_in, name="signin"),
	path('signout', views.sign_out, name="signout"),
	]
from django.urls import path
from . import views


urlpatterns = [
	
	#path('account', views.AccountView.as_view(), name="account"),
	#path('profile', views.profile_view, name="profile"),
	path('signup', views.sign_up_view, name="signup"),
	path('signin', views.sign_in_view, name="signin"),
	path('signout', views.sign_out_view, name="signout"),
	]
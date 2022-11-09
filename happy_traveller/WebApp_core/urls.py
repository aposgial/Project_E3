from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/templates/register/sign_in', views.login, name='login')
]
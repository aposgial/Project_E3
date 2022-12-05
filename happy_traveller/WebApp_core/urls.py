from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('place_details', views.place_details, name='place_details'),
]
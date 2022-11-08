from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('map', views.map, name='map'),
    path('maptest', views.maptest, name='maptest'),

    path('login2', views.login2, name='login2'),
]
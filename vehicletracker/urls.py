from django.urls import path
from .views import *

urlpatterns =  [
    path('getvehicle/',VehicleLocationListAPIView.as_view()),
    path('sendvehicledata/<pk>/',VehicleLocationUpdateAPIView.as_view()),
    path('getallvehicles/',VehicleLocationListAllVehiclesView.as_view()),
    path('getnearvehicles/',NearVehiclesListView.as_view()),
]
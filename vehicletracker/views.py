import datetime
import time

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from .models import VehicleLocation,Vehicle
from .serializers import VehicleLocationListSerializer, VehicleLocationSerializer
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import fromstr
from django.contrib.gis import measure


# Create your views here.
class VehicleLocationListAPIView(generics.ListAPIView):
    serializer_class = VehicleLocationListSerializer

    def get_queryset(self):
        vehicle = self.request.query_params.get('vehicle')
        vehicle = Vehicle.objects.get(vehicleID=vehicle).id
        return VehicleLocation.objects.filter(vehicle=vehicle).order_by('-timestamp')


class VehicleLocationListAllVehiclesView(generics.ListAPIView):
    serializer_class = VehicleLocationListSerializer
    queryset = VehicleLocation.objects.all()

class NearVehiclesListView(generics.ListAPIView):
    serializer_class = VehicleLocationListSerializer

    def get_queryset(self):
        latitude = self.request.query_params.get('latitude')
        longitude = self.request.query_params.get('longitude')
        current_point = fromstr('POINT(%s %s)' % (longitude,latitude))
        vehicles=VehicleLocation.objects.filter(loc__distance_lte=(current_point, measure.D(km=10))).annotate(distance=Distance('loc', current_point)).order_by('distance')
        return vehicles



class VehicleLocationUpdateAPIView(APIView):

    def get_object(self, pk):
        try:
            return Vehicle.objects.get(vehicleID=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        vehicle = self.get_object(pk)
        try:
            vehiclelocation = VehicleLocation.objects.get(vehicle=vehicle)
            data = request.data
            data = data.copy()
            data['vehicle'] = vehicle.id
            serializer = VehicleLocationSerializer(vehiclelocation, data=data)
        except VehicleLocation.DoesNotExist:
            id = Vehicle.objects.count()
            data = request.data
            data = data.copy()
            data['vehicle'] = int(id)+1
            serializer = VehicleLocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




from rest_framework import serializers
from .models import VehicleLocation


class VehicleLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleLocation
        fields = ['vehicle','lat', 'long', 'totalseats', 'availableseats', 'timestamp']


class VehicleLocationListSerializer(serializers.ModelSerializer):
    vehicle = serializers.SlugRelatedField(read_only=True,slug_field='vehicleID')
    class Meta:
        model = VehicleLocation
        fields = ['vehicle', 'lat', 'long', 'totalseats', 'availableseats','timestamp']

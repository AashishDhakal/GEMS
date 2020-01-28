from django.contrib import admin
from .models import *
# Register your models here.

class VehicleLocationModelAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'lat', 'long', 'totalseats', 'availableseats', 'timestamp']

    class Meta:
        model = VehicleLocation

class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ['vehicleName','vehicleID']

    class Meta:
        model = Vehicle


admin.site.register(VehicleLocation, VehicleLocationModelAdmin)

admin.site.register(Vehicle,VehicleModelAdmin)
from django.db import models
from django.contrib.gis.db import models


# Create your models here.
class Vehicle(models.Model):
    vehicleID = models.CharField(max_length=50)
    vehicleName = models.CharField(max_length=50)

    def __str__(self):
        return self.vehicleName

class VehicleLocation(models.Model):
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    totalseats = models.CharField(max_length=50)
    availableseats = models.CharField(max_length=50)
    loc = models.PointField(blank=True,geography=True,default='POINT(0.0 0.0)')

    objects = models.Manager()

    class Meta:
        verbose_name = "VehicleLocation"

    def __str__(self):
        return self.vehicle.vehicleName

    def save(self, *args, **kwargs):
        self.loc.y = self.latitude
        self.loc.x = self.longitude
        super(VehicleLocation, self).save(*args, **kwargs)

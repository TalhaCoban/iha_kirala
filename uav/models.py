from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User


# Create your models here.
class UAV(models.Model):
    company = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Company")
    model_name = models.CharField(max_length=100, verbose_name="Model Name")
    manufacturer = models.CharField(max_length=100, verbose_name="Manufacturer")
    uav_type = models.CharField(max_length=50, verbose_name="Type/Class")
    weight = models.FloatField(verbose_name="Weight (kg)")
    dimensions_length = models.FloatField(verbose_name="Length (m)")
    dimensions_width = models.FloatField(verbose_name="Width (m)")
    dimensions_height = models.FloatField(verbose_name="Height (m)")
    max_speed = models.FloatField(verbose_name="Maximum Speed (km/h)")
    range = models.FloatField(verbose_name="Range (km)")
    endurance = models.FloatField(verbose_name="Endurance (hours)")
    payload_capacity = models.FloatField(verbose_name="Payload Capacity (kg)")
    communication_range = models.FloatField(verbose_name="Communication Range (km)")
    navigation_system = models.CharField(max_length=100, verbose_name="Navigation System")
    camera_imaging_system = models.CharField(max_length=100, verbose_name="Camera/Imaging System")
    operating_altitude = models.FloatField(verbose_name="Operating Altitude (m)")
    takeoff_landing_method = models.CharField(max_length=100, verbose_name="Takeoff/Landing Method")
    control_interface = models.CharField(max_length=100, verbose_name="Control Interface")
    special_features = models.TextField(verbose_name="Special Features")
    rent_price_per_hour = models.FloatField(verbose_name="Rent Price Per Hour")

    def __str__(self):
        return self.model_name

    class Meta:
        verbose_name = "UAV"
        verbose_name_plural = "UAVs"
        
        

class RentedUAVs(models.Model):
    uavs = models.ManyToManyField(
        UAV,
        related_name="rented_uavs"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="rented_uavs"
    )
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    
    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        ordering = ["-startdate"]
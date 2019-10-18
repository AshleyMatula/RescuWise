from django.db import models

# Create your models here.

class Shelter(models.Model):
    shelter_name = models.CharField(max_length=200, default="unknown")
    location_gps_longitude = models.FloatField(null=True, blank=True, default=None)
    location_gps_latitude = models.FloatField(null=True, blank=True, default=None)
    address = models.CharField(max_length=200)

class  Animals(models.Model):
    animal_type = models.CharField(max_length=200)
    current_shelter = models.OneToOneField(Shelter,on_delete=models.CASCADE,)
 
from django.db import models

# Create your models here.

class Shelter(models.Model):
    shelter_name = models.CharField(max_length=200, default="unknown")
    # location_gps_longitude = models.FloatField(null=True, blank=True, default=None)
    # location_gps_latitude = models.FloatField(null=True, blank=True, default=None)
    address = models.CharField(max_length=200, default="unknown")
    phone = models.CharField(max_length=200, default='555-555-5555')
    email = models.EmailField(max_length=100, default='example@email.com')
    website = models.CharField(max_length=200, default="unknown")
    primary_contact = models.CharField(max_length=200, default="unknown")

    def __str__(self):
        return self.shelter_name

class Animal(models.Model):
    animal_type = models.CharField(max_length=200, default="unknown")
    current_shelter = models.OneToOneField(Shelter, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='images/default.jpg', upload_to='images/')
    breed = models.CharField(max_length=200, default="unknown")
    color = models.CharField(max_length=200, default="unknown")
    age = models.IntegerField()
    euth_date = models.DateField()
    id_number = models.CharField(max_length=200, default="unknown")
    current_pledges = models.IntegerField()
    goal = models.IntegerField()
    neutered_spayed = models.BooleanField()
    name = models.CharField(max_length=200, default="unknown")
    description = models.TextField()
    hw = models.BooleanField()
    surrender_reason = models.CharField(max_length=200, default="unknown")
    weight = models.IntegerField()

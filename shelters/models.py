from django.db import models

class Shelter(models.Model):
    shelter_name = models.CharField(max_length=200, default="unknown")
    address = models.CharField(max_length=200, default="unknown")
    phone = models.CharField(max_length=200, default='555-555-5555')
    email = models.EmailField(max_length=100, default='example@email.com')
    website = models.CharField(max_length=200, default="unknown")
    primary_contact = models.CharField(max_length=200, default="unknown")

    def __str__(self):
        return self.shelter_name

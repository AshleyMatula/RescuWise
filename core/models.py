from django.db import models
from core.model_lists import *
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Shelter(models.Model):
    shelter_name = models.CharField(max_length=200, default="unknown")
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
    profile_picture = models.ImageField(default='images/default.png', upload_to='images/')
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

    def __str__(self):
        return f"{self.id_number} {self.name} - {self.current_shelter}"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    organization = models.CharField(verbose_name="Name",max_length=100, blank=False,)
    location_city = models.CharField(verbose_name="City",max_length=100, blank=True,)
    location_state = models.CharField(verbose_name="State",choices=state_validation_choices,max_length=2, blank=True,)
    user_type = models.TextField(verbose_name="Which of the following best describes you:",choices=user_type_choices,blank=False,default="",)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    terms_agree = models.TextField(blank=True,default="",verbose_name="I agree to the website's Privacy Policy & Terms and Conditions.")
    main_picture = models.ImageField(verbose_name="Profile Picture",upload_to='media/',default='images/default.png',blank=True,)
    is_published = models.BooleanField(default=True,verbose_name='Would you like others to view your profile? ')
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

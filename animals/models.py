from django.db import models
from shelters.models import Shelter

class Animal(models.Model):
    animal_type = models.CharField(max_length=200, default="unknown")
    current_shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
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

    # calculate percentage of goal completed and convert to int
    # to be easily referenced in templates as .goal_percent
    # (i'm leaving it as a multiline for readability)
    def goal_percent(self):
        gp = self.current_pledges / self.goal
        gp = gp * 100
        gp = int(gp)
        return gp
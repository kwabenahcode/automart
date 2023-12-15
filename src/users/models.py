from django.db import models
from django.contrib.auth.models import User 



class Locations(models.Model):
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    
#The profile model below is linked to the user model. The cascade function inherited,
#help to delete the profile once the user model is deleted 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(null=True)
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=13, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    
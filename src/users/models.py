from django.db import models
from django.contrib.auth.models import User 

#The below is 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
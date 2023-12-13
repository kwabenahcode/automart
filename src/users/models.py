from django.db import models
from django.contrib.auth.models import User 

#The profile model below is linked to the user model. the cascade function inherited,
#help to delete the profile once the user model is deleted 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
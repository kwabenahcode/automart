from django.db import models
from django.contrib.auth.models import AbstractUser 

from localflavor.gh.models import GHRegionField
from localflavor.us.models import USZipCodeField

from .utils import user_photo_directory_path


class User(AbstractUser):
    address_1 = models.CharField(max_length=128, blank=True,null=True)
    address_2 = models.CharField(max_length=128, blank=True,null=True)
    city = models.CharField(max_length=64,blank=True,null=True)
    region = GHRegionField(default='GR')
    zip_code = USZipCodeField(blank=True,null=True)
    photo = models.ImageField(upload_to=user_photo_directory_path, null=True, blank=True)
    bio = models.CharField(max_length=140, blank=True,null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    
    def __str__(self):
        return self.username

    
    
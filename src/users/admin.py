from django.contrib import admin

from .models import Profile

#Registered the Profile model so that, the admin module can recognize it.
class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
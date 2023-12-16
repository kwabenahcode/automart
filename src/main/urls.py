from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name="main"),
    path('user_registration', views.user_registration, name="user_registration"),
    
]

from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('user_registration', views.user_registration, name="user_registration"),
]

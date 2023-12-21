from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.models import *



def main_view(request):
    return render(request, 'views/main.html')

def home_view(request):
    return render(request, 'views/home.html')



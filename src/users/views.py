from django.shortcuts import render, redirect
from http.client import HTTPResponse
from .models import User
from django.contrib import messages

def login_view(request):
    return HTTPResponse('Login View: ')

def user_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if User.objects.filter(username=username):
            messages.error(request, f"{username} Already Exist")
            return redirect (request.META.get("HTTP_REFERER"))
        
        
        if password1 != password :
            messages.error(request, f"Password Mismatch")
            return redirect (request.META.get("HTTP_REFERER"))
        
        
        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            )
        user.set_password(password)
        user.save()
        messages.success(request, f'Hello {first_name} you have successfully created an account')
    return render(request, 'views/register.html')


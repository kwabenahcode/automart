from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not  None:
                pass
            else:
                pass
            print(user)
    elif request.method == 'GET':
        login_form = AuthenticationForm()
    return render(request, 'users/login.html', {"login_form":login_form})

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
    return render(request, 'users/register.html')


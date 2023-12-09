from django.shortcuts import render
from django.http import HttpResponse

def main_view(request):
    return HttpResponse('<h1>Hello World</h1>')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'home/Home.html')

def aboutUs(request):
    return render(request, 'home/aboutUs.html')

def contactUs(request):
    return render(request, 'home/contactUs.html')





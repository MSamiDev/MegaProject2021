from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *

# Create your views here.

def index(request):
    blog_posts = Blog.objects.all()
    context = {'blog_posts': blog_posts}
    return render(request, 'home/Home.html', context)

def aboutUs(request):
    return render(request, 'home/aboutUs.html')

def contactUs(request):
    return render(request, 'home/contactUs.html')





from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    blog_posts = Blog.objects.all()
    #context = {'blog_posts': blog_posts}
    blog_pagination = Paginator(blog_posts, 9)
    page_number = request.GET.get('page')
    try:
        page_obj = blog_pagination.get_page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = blog_pagination.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = blog_pagination.page(blog_pagination.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'blog/Blog-Page.html', context)


def blog(request):
    return render(request, 'blog/Blog-Post.html')
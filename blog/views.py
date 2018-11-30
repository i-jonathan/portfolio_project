from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    bpost = Blog.objects
    return render(request, 'blog/allblogs.html', {'blog': bpost})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})
# Create your views here.

from django.shortcuts import render,redirect
from .models import Post, Comment, Like
# Create your views here.
#!  ---------HOME----------
def home(request):
    posts=Post.objects.all()
    context={
        "posts":posts
    }
    return render(request, 'blog/home.html',context)

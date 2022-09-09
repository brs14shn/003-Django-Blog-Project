from django.shortcuts import render,redirect
from .models import Post, Comment, Like
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
# Create your views here.
#!  ---------HOME----------
def home(request):
    posts=Post.objects.all()
    context={
        "posts":posts
    }
    return render(request, 'blog/home.html',context)

#TODO  CRUD/CREATE(POST)---------BLOG-ADD----------
@login_required(login_url ='/auth/login')
def post_add(request):
    form=NewPostForm()
    if request.method=="POST":
        form=NewPostForm(request.POST)
        if form.is_valid():
           postform=form.save()
           if "post_image" in request.FILES:
                postform.post_image=request.FILES.get("post_image")
                postform.post_image.save()
           return redirect("home")

    context={
        "form":form
    }
    return render(request,"blog/blog_add.html",context)

#!-------------UPDATE----------
def post_update(request,id ):
    post=Post.objects.get(id=id)
    form=NewPostForm(instance=post)
    if request.method=='POST':
        form=NewPostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context={
        'form':form
    }
    return render(request,'blog/blog.html',context)
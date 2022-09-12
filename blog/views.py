from django.shortcuts import render,redirect
from .models import Post, Comment, Like
from .forms import NewPostForm,CommentForm
from django.contrib.auth.decorators import login_required

# import datetime

from datetime import datetime

# a = datetime.strptime('8/18/2008', date_format)
# b = datetime.strptime('9/26/2008', date_format)
# Create your views here.
#!  ---------HOME----------
def home(request):
    posts=Post.objects.all()
    date_format = "%Y/%m/%d"
    currentdate=datetime.strptime('2022/09/12', date_format)
    print(currentdate)
    context={
        "posts":posts,
        "currentdate":currentdate
    }
    return render(request, 'blog/home.html',context)
    # posts=[]
    # if request.user.is_authenticated:
    #     posts=Post.objects.filter(user=request.user)
    # form=NewPostForm()
    # context={
    #     "posts":posts,
    #     "form":form
    # }
    # return render(request, 'blog/home.html',context)

def about_page(request):
       return render(request, 'blog/about.html')

#TODO  CRUD/CREATE(POST)---------BLOG-ADD----------

def post_add(request):
    form=NewPostForm()
    if request.method=="POST":
        form=NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        #    postform=form.save()
        #    if "post_image" in request.FILES:
        #         postform.post_image=request.FILES.get("post_image")
        #         postform.post_image.save()
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
    return render(request,'blog/blog_update.html',context)


@login_required(login_url ='/auth/login')
def post_detail(request, id):        
    post = Post.objects.get(id=id)
    comment_form = CommentForm()
    comments = Comment.objects.filter(post=post.id)
    post.blog_views += 1
    post.save()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            post.blog_comment += 1
            comment.user = request.user
            post.save()
            comment.save()
            return redirect('detail', id=id)
    context = {
        'post':post, 'comment_form':comment_form, 'comments':comments}
    return render(request, 'blog/blog_detail.html', context)
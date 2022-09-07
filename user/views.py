from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import UserForm, UserProfileForm

from django.contrib import messages

# Create your views here.

def register(request):
    form_user=userForm()
    form_profile=UserProfileForm()
    if request.method=="POST":
        form_user=UserForm(request.POST)
        form_profile=UserProfileForm(request.POST,request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            user=form_user.save()
            profile=form_profile.save(commit=False) 
            profile.user=user
            profile.save()

            login(request,user)
            messages.success(request,'Register Successfull')

            return redirect('blog_list') 
    context={
        'form_profile':form_profile,
        'form_user':form_user
    }
    return render(request,'user/register.html',context)

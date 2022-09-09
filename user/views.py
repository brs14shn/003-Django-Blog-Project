from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from user.forms import UserForm, UserProfileForm

from django.contrib import messages

#Create your views here.
def logout(request):
     messages.success(request, 'You logged out') 
     logout(request)
     return redirect('home')


def register(request):
    form_user=UserForm()
    form_profile=UserProfileForm()
    if request.method=="POST":
        form_user=UserForm(request.POST)
        form_profile=UserProfileForm(request.POST,request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            user=form_user.save()
            profile=form_profile.save(commit=False) 
            profile.user=user
            profile.save()

            # login(request,user)
            messages.success(request,'Register Successfull')

            return redirect('home') 
    context={
        'form_profile':form_profile,
        'form_user':form_user
    }
    return render(request,'user/register.html',context)



def login(request):
    form=AuthenticationForm(request,data=request.POST)
    if form.is_valid():
        user=form.get_user()
        login(request, user)
        if user:
            messages.success(request,'login successful')
            return redirect('home')
    else:
       form=AuthenticationForm() 

    return render(request,'user/login.html',{'form':form})

def profile_page(request):
    profile = UserCreationForm(request.POST)

    return render(request, 'user/profile_page.html', {'profile': profile})
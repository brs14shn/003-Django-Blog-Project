from django.urls import path
from .views import (
    register,
    user_login,
    user_logout,
    profile_page,
   
)
#from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("register/",register,name="register"),
    path("login/",user_login,name="login"),
    path('logout/',user_logout,name='logout'),
    #path("logout",LogoutView.as_view(),name="logout_app"),
    path('profile', profile_page, name="profile"),
    
]

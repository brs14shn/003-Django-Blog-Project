from django.urls import path
from .views import (
    register,
    login,
    # logout,
    profile_page,
   
)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("register/",register,name="register"),
    path("login/",login,name="login"),
    # path('logout/',logout,name='logout'),
    path("logout",LogoutView.as_view(),name="logout_app"),
    path('profile', profile_page, name="profile"),
    
]

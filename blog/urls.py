from django.urls import path
from .views import (
    home,
    post_add,
)


urlpatterns = [
    path("",home,name="home"),
    path('post_add/',post_add,name='add'),
] 

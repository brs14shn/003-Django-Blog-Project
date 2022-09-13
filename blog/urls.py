from django.urls import path
from .views import (
    home,
    post_add,
    post_update,
    post_detail,
    about_page,
    post_delete
)


urlpatterns = [
    path("",home,name="home"),
    path('post_add/',post_add,name='add'),
    path('update/<int:id>', post_update, name='update'),
    path('detail/<int:id>', post_detail, name='detail'),
    path('about', about_page, name='about'),
     path('delete/<int:id>', post_delete, name='delete'),

] 

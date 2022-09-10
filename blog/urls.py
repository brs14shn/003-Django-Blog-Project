from django.urls import path
from .views import (
    home,
    post_add,
    post_update,
    post_detail
)


urlpatterns = [
    path("",home,name="home"),
    path('post_add/',post_add,name='add'),
    path('update/<int:id>', post_update, name='update'),
    path('detail/<int:id>', post_detail, name='detail'),

] 

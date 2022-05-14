from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   # path('',views.demo,name='demo'),
   # path('register/',views.register,name='register'),

    #CRUD

    path('posts/',views.post_index,name='post_index'),
    path('edit/<int:post_id>/',views.post_edit,name='post_edit'),
    path('show/<int:post_id>/',views.post_show,name='post_show'),
    path('',views.post_create,name='post_create'),
    path('update/',views.post_update,name='post_update'),
    path('delete/<int:post_id>/',views.post_delete,name='post_delete'),
]

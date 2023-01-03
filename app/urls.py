from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('add_todo/', add_todo, name='add_todo'),
    path('complete_todo/<int:todo_id>/', complete_todo, name='complete_todo'),
    path('delete_todo/<int:todo_id>/', delete_todo, name='delete_todo'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('about/', about, name='about'),
]

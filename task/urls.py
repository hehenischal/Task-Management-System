from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('manager', manager_index,name="manager_home"),
    path('create_task',assign_task, name="assign_task"),
    
]

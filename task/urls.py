from django.urls import path
from .views import *

urlpatterns = [
    path('home', index,name='home'),
    path('manager', manager_index),
    path('my_task',my_task,name='my_task'),
    path('submit_task/', submit_task_file, name='uploadfile'),
    path('profile/', view_profile, name='view_profile')

   
]

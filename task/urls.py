from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='home'),
    path('manager', manager_index),
    path('my_tasks',my_task,name='my_tasks'),
    path('submit_task/', submit_task_file, name='uploadfile'),
     path('profile/', view_profile, name='view_profile')

   
]

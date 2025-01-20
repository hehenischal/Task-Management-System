from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('manager', manager_index),
    path('my_tasks',my_task),
    path('submit_task/', submit_task_file, name='uploadfile')

   
]

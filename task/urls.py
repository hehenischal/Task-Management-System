from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('manager/', manager_index, name='manager'),
    path('assign_task/', assign_task, name='assign_task' ),
    path('my_tasks/',my_task,name='my_tasks'),
    path('submit_task/', submit_task_file, name='uploadfile'),
    path('add_employee/', add_employee, name='add_employee' ),
    path('login_view/' ,login_view, name="login_view"),
    path('logout_view/', logout_view, name="logout_view"),

]

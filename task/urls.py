from django.urls import path
from .views import *

urlpatterns = [
    path('',redirects),
    path('home/', index,name='home'),
    path('my_task/',my_task,name='my_task'),
    path('manager_home/', manager_index, name='manager_home'),
    path('assign_task/', assign_task, name='assign_task' ),
    path('add_employee/', add_employee, name='add_employee' ),
    path('login_view/' ,login_view, name="login_view"),
    path('logout_view/', logout_view, name="logout_view"),
    path('submit_task/<int:id>/', submit_task_file, name='uploadfile'),
    path('view_profile/', view_profile, name='view_profile'),
    path('set_password/', set_password1, name='set_password'),
    path('to_review/', to_review, name='to_review'),
    path('task_completed/<int:id>/', task_completed, name='mark_completed'),
    path('completed_task/', completed_task, name='completed_task'),
    path('send_email/', send_email_view, name='send_email'),
    path('mark_revision/<int:id>/', mark_revision, name='mark_revision'),


   
]

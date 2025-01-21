from django.contrib import admin
from .models import CustomUser, Task, File, Employee

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Task)
admin.site.register(File)

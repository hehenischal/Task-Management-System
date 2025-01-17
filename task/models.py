from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_employee = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.username


status_choices = (
    ('Pending', 'Pending'),
    ('In review', 'In review'),
    ('needs revision', 'needs revision'),
    ('Completed', 'Completed')
)

class Task(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    assigner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigner')
    assignee = models.ManyToManyField(CustomUser, related_name='assignee')

    def __str__(self):
        return self.title
    
class File(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.task.title
    
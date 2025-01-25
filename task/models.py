from django.db import models
from django.contrib.auth.models import AbstractUser, User
from decouple import config
from django.core.mail import send_mail

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_employee = models.BooleanField(default=True)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.username


status_choices = (
    ('Pending', 'Pending'),
    ('In review', 'In review'),
    ('Needs revision', 'Needs revision'),
    ('Completed', 'Completed')
)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()  # Added the description field here
    status = models.CharField(max_length=100, choices=status_choices, default='Pending')
    date = models.DateTimeField(auto_now_add=True)
    assigner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigner')
    assignee = models.ManyToManyField(CustomUser, related_name='assignee')
    due_date = models.DateField()
    priority = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])

    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    #     subject = 'Task Completed'
    #     message = f'Your task{self.title} has updated to the status of {self.status}'
    #     from_email = config('EMAIL_HOST_USER')  # Sender's email address
    #     recipient_list = ['task.assignee.email'] # Recipient's email address
    #     #recipient_list = [task.assignee.email]  # Recipient's email address
        
    #     send_mail(subject, message, from_email, recipient_list)
        
    #     super().save(*args, **kwargs)

from django.conf import settings
import os
class File(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name  
    
    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.file.name))
        super().delete(*args, **kwargs)

class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)  
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15) 
    address = models.TextField()
    post = models.CharField(max_length=100) 
    start_date = models.DateField()  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
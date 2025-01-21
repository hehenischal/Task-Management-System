from django import forms
<<<<<<< HEAD
from .models import Task

class TaskForm(forms.ModelForm):
     class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter task title'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control', 
                'type': 'datetime-local'
            }),
            'assigner': forms.Select(attrs={
                'class': 'form-select'
            }),
            'assignee': forms.SelectMultiple(attrs={
                'class': 'form-select', 
                'size': 5  # Allows multiple selections
            })
        }
labels = {
            'title': 'Task Title',
            'status': 'Task Status',
            'date': 'Date Assigned',
            'assigner': 'Assigned By',
            'assignee': 'Assigned To'
        }
=======
from .models import File
 
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
>>>>>>> be2126149f3c27b1dd55ee30d1f43e0a66

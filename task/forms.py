from django import forms
from .models import Task,File,CustomUser,Employee
forms.Form
class EmployeeForm(forms.ModelForm):
     class Meta:
        model = Task
        fields = '__all__'

        
class Fileform (forms.ModelForm):
     class Meta:
        model = File
        fields = '__all__'
        labels={
            'file':'upload file',
            'description':'file description'
        }


class TaskForm(forms.ModelForm):
     class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter task title'
            }),
            'description':forms.Textarea(attrs={
                'class':'form-control'
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
                'size': 5  
            })
        }
labels = {
            'title': 'Task Title',
            'status': 'Task Status',
            'date': 'Date Assigned',
            'assigner': 'Assigned By',
            'assignee': 'Assigned To'
        }


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'is_employee', 'is_manager']

    is_employee = forms.BooleanField(required=False)
    is_manager = forms.BooleanField(required=False)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['is_employee'].required = True
    #     self.fields['is_manager'].required = False

    def clean(self):
        cleaned_data = super().clean()
        is_employee = cleaned_data.get('is_employee')
        is_manager = cleaned_data.get('is_manager')

        # Ensure a user can't be both employee and manager at the same time
        if is_employee and is_manager:
            raise forms.ValidationError("A user cannot be both employee and manager.")
        return cleaned_data
        



class Fileform(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
        widgets = {
            'task': forms.HiddenInput(),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter file name'
            }),
            'file': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }
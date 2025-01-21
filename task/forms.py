from django import forms
from .models import File, Employee
 
class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'
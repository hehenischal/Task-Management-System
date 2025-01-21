from django.shortcuts import render,redirect
from .forms import TaskForm, FileForm, AddEmployeeForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request,'employeebase.html')

def manager_index(request):
    return render(request, 'manager_base.html')

def assign_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
       
        if form.is_valid():
            form.save()
            return redirect("manager_home")
    else:
        form = TaskForm()

    return render(request, "create_task.html", {'form': TaskForm})

def add_employee(request):
    if request.method == 'POST':
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('manager_home')  
    else:
        form = AddEmployeeForm()

    return render(request, 'add_employee.html', {'form': AddEmployeeForm})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
    
            if user is not None:
                login(request, user)
                return redirect('manager_home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('manager_home')
    return render(request,'logout.html')




def my_task(request): 
    employee_obj = request.user
    context = {
        'employee': employee_obj
    } 
    return render(request, 'assigntask.html', context)

def submit_task_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.employee = request.user
            form.save()
            return redirect('task_list') 
    else:
        form = FileForm()
    
    return render(request, 'uploadfile.html', {'form': form})

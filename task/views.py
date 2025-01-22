from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee,CustomUser,Task,File
from .forms import TaskForm,AddEmployeeForm,Fileform,EmployeeForm
from django.contrib.auth import authenticate, login,logout,get_user_model
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password



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
           user =  form.save() 
           user.set_password('defaultpassword')
           user.save()
           messages.success(request, "Employee added successfully!")
           return redirect('manager_home')  
        
        else:
            messages.error(request, "There was an error with the form. Please try again.")
    else:
        form = AddEmployeeForm()

    return render(request, 'add_employee.html', {'form': AddEmployeeForm})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "Both fields are required!")
            return render(request, "login.html")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Check if the employee is using the default password
            if check_password(password, user.password):  
                return redirect("set_password")  # Redirect to password change page
            
            if user.is_staff:  
                return redirect("manager_home")  # Redirect managers to dashboard
            else:
                return redirect("home")  # Redirect employees to home

        else:
            messages.error(request, "Invalid username or password!")

    return render(request, "login.html")

@login_required
def set_password(request):
    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password == confirm_password:
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, "Password updated successfully! Please log in again.")
            return redirect("login_view")  # Redirect to login

    return render(request, "set_password.html")





def logout_view(request):
    logout(request)
    return redirect('login_view') 


@login_required
def to_review(request):
    if not request.user.is_manager:
        return redirect('home')
    
    tasks = Task.objects.filter(status='to_review')
    return render(request, 'to_review.html',{'tasks':Task})


def my_task(request): 
    employee_obj = request.user
    context = {
        'employee': employee_obj
    } 
    return render(request, 'my_task.html', context)

def submit_task_file(request):
    if request.method == 'POST':
        form = Fileform(request.POST, request.FILES)
        if form.is_valid():
            form.instance.employee = request.user
            form.save()
            return redirect('task_list') 
    else:
        form = Fileform()
    
    return render(request, 'uploadfile.html', {'form': form})

def view_profile(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST) 
        if form.is_valid():
            form.save()  
            return redirect('view_profile')  
    else:
        form = EmployeeForm()

    return render(request, 'viewprofile.html', {'form': form})
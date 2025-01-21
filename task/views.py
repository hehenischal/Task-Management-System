from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee,CustomUser,Task,File
from .forms import TaskForm,AddEmployeeForm,Fileform,EmployeeForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,SetPasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages



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
    if request.user.is_authenticated:
        return redirect('manager_home')  # Redirect if already logged in

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            try:
                user = CustomUser.objects.get(username=username)
                
                if user.password:  # User has a password set
                    # Authenticate and log in
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        messages.success(request, "Login successful!")
                        return redirect('manager_home')
                else:
                    # If no password set, show password form
                    if 'set_password' in request.POST:
                        password_form = SetPasswordForm(user, data=request.POST)
                        if password_form.is_valid():
                            password_form.save()
                            login(request, user)
                            messages.success(request, "Password set successfully!")
                            return redirect('manager_home')
                        else:
                            messages.error(request, "There was an issue with setting the password.")
                            return render(request, 'login.html', {'form': form, 'password_form': password_form})

                    # Redirect to set password if no password exists
                    password_form = SetPasswordForm(user)
                    return render(request, 'login.html', {'form': form, 'password_form': password_form})

            except User.DoesNotExist:
                messages.error(request, "Invalid username or password.")
                return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login_view') 




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
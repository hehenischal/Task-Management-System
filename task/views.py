from django.shortcuts import render,redirect
from .models import CustomUser 
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm, TaskForm,Fileform
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

    return render(request, "create_task.html", {"form": TaskForm})




def my_task(request ): 
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
from django.shortcuts import render,redirect
from .models import CustomUser 
from .forms import FileForm
# Create your views here.
def index(request):
    

    return render(request,'employeebase.html')

def manager_index(request):
    return render(request, 'manager_base.html')


def my_task(request ): 
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

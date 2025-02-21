from django.shortcuts import render, get_object_or_404, redirect
from .models import Department
from .forms import DepartmentForm

# List all departments
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/department_list.html', {'departments': departments})

# Add a new department
def department_add(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'departments/department_form.html', {'form': form})

# Edit a department
def department_edit(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'departments/department_form.html', {'form': form})

# Delete a department
def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'departments/department_confirm_delete.html', {'department': department})

# ===============================================================

    

def department_view(request, pk):
    department = get_object_or_404(Department, pk=pk)
    return render(request, 'departments/department_view.html', {'department': department})
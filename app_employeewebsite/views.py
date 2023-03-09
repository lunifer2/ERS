from django.shortcuts import render, redirect
from .forms import EmployeeCreateForm
from .models import Employee, User, Department
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def employee_index(request):
    """ Returns list of employee as context """

    employee_list = Employee.objects.all()
    context = {"data": employee_list}
    
    if request.method == "POST":
        dataList = Employee.objects.filter(full_name=request.POST.get('full_name'))
        context.update({"data": dataList})
        return render(request, 'employees/index_employee.html', context)
    
    return render(request, 'employees/index_employee.html', context)

def employee_add(request):
    emp_create_form = EmployeeCreateForm()
    context = {"form": emp_create_form}

    if request.method == "POST":
        emp = Employee()
        user = User.objects.get(id=request.POST.get('user'))
        department = Department.objects.get(id=request.POST.get('department'))

        emp.full_name = request.POST.get('full_name')
        emp.address = request.POST['address']
        emp.blood_group = request.POST.get('blood_group')
        emp.contact = request.POST.get('contact')
        emp.email = request.POST.get('email')
        emp.dob = request.POST.get('dob')
        emp.gender = request.POST.get('gender')
        emp.join_date = request.POST.get('join_date')
        emp.user = user
        emp.department = department
        emp.save()

        messages.success(request, 'Employee added successfully')

        return redirect('emp-index')
    return render(request, 'employees/add_employee.html', context)

def employee_edit(request, id):
    data = Employee.objects.get(id=id)
    department = Department.objects.all()
    user = User.objects.all()

    context = {"data": data, "department": department, "user": user}
    return render(request, 'employees/edit_employee.html', context)

def employee_update(request):
    if request.method == "POST":
        user = User.objects.get(id=request.POST.get('user'))
        department = Department.objects.get(id=request.POST.get('department'))
        emp = Employee.objects.get(id=request.POST.get('id'))
        emp.full_name = request.POST.get('full_name')
        emp.address = request.POST.get('address')
        emp.blood_group = request.POST.get('blood_group')
        emp.contact = request.POST.get('contact')
        emp.email = request.POST.get('email')
        emp.dob = request.POST.get('dob')
        emp.gender = request.POST.get('gender')
        emp.join_date = request.POST.get('join_date')
        emp.user = user
        emp.department = department
        emp.save()
    return redirect("emp-index")

def employee_delete(request, id):
    data = Employee.objects.get(id=id)
    data.delete()
    return redirect("emp-index")

def employee_show(request, id):
    data = Employee.objects.get(id=id)
    context = {"data": data}
    return render(request, 'employees/show_employee.html', context)
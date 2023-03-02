from django.shortcuts import render, redirect
from .forms import EmployeeCreateForm, DepartmentCreateForm, EmployeeAttendanceForm, EmployeeSalaryForm
from .models import Employee, User, Department, EmployeeSalary
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def employee_index(request):
    ''' Returns list of employee as context'''

    employee_list = Employee.objects.all()
    context = {'data': employee_list}

    return render(request, 'employees/index_employee.html', context)


def employee_add(request):
    """ Adds employee """

    emp_create_form = EmployeeCreateForm()
    context = {"form": emp_create_form}
    if request.method == "POST":
        emp = Employee()
        user = User.objects.get(id=request.POST.get('user'))
        department = Department.objects.get(id=request.POST.get('department'))
        emp.full_name = request.POST.get('full_name')
        emp.address = request.POST.get('address')
        emp.contact = request.POST.get('contact')
        emp.email = request.POST.get('email')
        emp.dob = request.POST.get('dob')
        emp.join_date = request.POST.get('join_date')
        emp.blood_group = request.POST.get('blood_group')
        emp.gender = request.POST.get('gender')
        emp.user = user
        emp.department = department
        emp.save()
        messages.success(request, "Employee added succesfully")
        return redirect('emp-index')
    return render(request, 'employees/add_employee.html', context)


def employee_delete(request, id):
    data = Employee.objects.get(id=id)
    data.delete()
    return redirect("emp-index")


def employee_update(request):
    if request.method == "POST":
        user = User.objects.get(id=request.POST.get('user'))
        department = Department.objects.get(id=request.POST.get('department'))
        emp = Employee.objects.get(id=request.POST.get('id'))
        # form ko name bata value tanxa
        emp.full_name = request.POST.get('full_name')
        emp.address = request.POST.get('address')
        emp.contact = request.POST.get('contact')
        emp.email = request.POST.get('email')
        emp.dob = request.POST.get('dob')
        emp.join_date = request.POST.get('join_date')
        emp.blood_group = request.POST.get('blood_group')
        emp.gender = request.POST.get('gender')
        emp.user = user
        emp.department = department
        emp.save()
    return redirect("emp-index")


def employee_edit(request, id):
    data = Employee.objects.get(id=id)
    department = Department.objects.all()
    user = User.objects.all()
    context = {"data": data, "department": department, "user": user}
    return render(request, 'employees/edit_employee.html', context)


def employee_show(request, id):
    data = Employee.objects.get(id=id)
    context = {"data": data}
    return render(request, 'employees/show_employee.html', context)

# For departments


def department_index(request):
    ''' Returns list of department as context'''

    dep_list = Department.objects.all()
    context = {'data': dep_list}

    return render(request, 'departments/index_department.html',context)

def department_delete(request, id):
    ''' Deletes the data from department '''

    data = Department.objects.get(id=id)
    data.delete()

    return redirect("dep-index")

def department_add(request):
    ''' Adds the department '''

    dep_create_form = DepartmentCreateForm()
    context = {"form": dep_create_form}
    if request.method == "POST":
        dep = Department()
        dep.department_name = request.POST.get("department_name")
        dep.short_name = request.POST.get("short_name")
        # dep.status = request.POST.get("status")
        dep.save()
        messages.success(request, "Department added succesfully")
        return redirect('dep-index')

    return render(request, 'departments/add_department.html', context)


def department_edit(request, id):
    ''' Edits the data in department '''

    data = Department.objects.get(id=id)
    context = {"data": data}
    
    return render(request, 'departments/edit_department.html', context)

def department_update(request):
    if request.method == "POST":
     ''' This updates the data of departments '''

     dep = Department.objects.get(id=request.POST.get('id'))
     dep.department_name = request.POST.get("department_name")
     dep.short_name = request.POST.get("short_name")
     dep.status = request.POST.get("status")
     dep.save()
     messages.success(request, "Department added succesfully")
     return redirect('dep-index')
    

def department_show(request, id):
    data = Department.objects.get(id=id)
    context = {"data": data}
    return render(request, 'departments/show_department.html', context)

# For Salary


def salary_record_index(request):
    ''' Returns list of salary record as context'''

    salary_list = EmployeeSalary.objects.all()
    context = {'data': salary_list}

    return render(request, 'salaryrecords/index_salary_record.html', context)


def salary_record_add(request):
    salary_create_form = EmployeeSalaryForm()
    context = {"form": salary_create_form}
    ''' Adds the salary record '''
    if request.method == "POST":
        salary = EmployeeSalary()
        employee = Employee.objects.get(id=request.POST.get('employee'))
        salary.salary_amount = request.POST.get("salary_amount")
        salary.bonus_amount = request.POST.get("bonus_amount")
        salary.allowance = request.POST.get("allowance")
        salary.tds_in_percent =request.POST.get("tds_in_percent")
        salary.start_date = request.POST.get("start_date")
        salary.end_date = request.POST.get("end_date")
        salary.employee = employee
        # salary.status = request.POST.get("status")
        salary.save()
        messages.success(request, "Salary Record added succesfully")
        return redirect('salary-index')
    return render(request, 'salaryrecords/add_salary_record.html', context)


def salary_record_edit(request, id):
    ''' Edits the salary record of employee '''

    data = EmployeeSalary.objects.get(id=id)
    context = {"data": data}
    return render(request, 'salaryrecords/edit_salary_record.html', context)


def salary_record_show(request, id):
    data = EmployeeSalary.objects.get(id=id)
    context = {"data": data}
    return render(request, 'salaryrecords/show_salary_record.html', context)

def salary_record_update(request):
   if request.method == "POST":
        salary = EmployeeSalary.objects.get(id=request.POST.get('id'))
        # employee = Employee.objects.get(id=request.POST.get('employee'))
        salary.salary_amount = request.POST.get("salary_amount")
        salary.bonus_amount = request.POST.get("bonus_amount")
        salary.allowance = request.POST.get("allowance")
        salary.tds_in_percent =request.POST.get("tds_in_percent")
        salary.start_date = request.POST.get("start_date")
        salary.end_date = request.POST.get("end_date")
        # salary.employee = employee
        # salary.status = request.POST.get("status")
        salary.save()
        messages.success(request, "Salary Record added succesfully")
        return redirect('salary-index')

def salary_record_delete(request, id):
    ''' Deletes the data from department '''

    data = EmployeeSalary.objects.get(id=id)
    data.delete()

    return redirect("salary-index")
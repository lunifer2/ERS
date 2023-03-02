from django import forms
from .models import Employee, Department, EmployeeAttendance, EmployeeSalary

class EmployeeCreateForm(forms.ModelForm):
    """ Form class for employee creation """
    class Meta:
        fields = "__all__"
        # fields = ("fullname","contact")
        model = Employee

class DepartmentCreateForm(forms.ModelForm):
    """ Form class for department creation """
    class Meta:
        fields = "__all__"
        model = Department

class EmployeeAttendanceForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = EmployeeAttendance

class EmployeeSalaryForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = EmployeeSalary


from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.short_name

    class Meta:
        db_table = "app_department"

class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    email = models.EmailField()
    dob = models.DateField()
    join_date = models.DateField()
    gender = models.CharField(max_length=255)
    blood_group = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        db_table = 'app_employee'

    def __str__(self):
        return self.full_name
        
class EmployeeAttendance(models.Model):
    status = models.BooleanField(default=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    attend_date = models.DateField()
    check_in_time = models.CharField(max_length=255)
    check_out_time = models.CharField(max_length=255)

    class Meta:
        db_table = 'app_employee_attendance'

class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_amount = models.FloatField()
    bonus_amount = models.FloatField(default=0)
    allowance = models.FloatField(default=0)
    tds_in_percent = models.FloatField(default=1)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'app_employee_salary'
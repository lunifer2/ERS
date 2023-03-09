from rest_framework import serializers
from app_employeewebsite.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "full_name", "contact", "email", "dob", "join_date", "gender", "address","blood_group","department", "user")
from django.shortcuts import render
from .serializers import EmployeeSerializer
from app_employeewebsite.models import Employee, Department

from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from django.contrib.auth.models import User

# Create your views here.
class CustomReponse():
    def successResponse(self, code, msg, data=dict()):
        context = {
            "status_code": code,
            "message": msg,
            "data": data,
            "error": []
        }
        return context
    
    def errorResponse(self, status_code, msg, error=dict()):
        res = {
            "status_code": status_code,
            "message": msg,
            "data": [],
            "error": error
        }
        return res
    
class EmployeApiView(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serialier = EmployeeSerializer(employee, many=True)
        return Response(CustomReponse.successResponse(200,"Employee List", serialier.data), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(CustomReponse.successResponse(200, "Added successfully", serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(CustomReponse.errorResponse(408, "Validation Error", serializer.errors), status=status.HTTP_408_REQUEST_TIMEOUT)

class EmployeeApiIdView(APIView):
    def get_object(self, id):
        try:
            data = Employee.objects.get(id=id)
            return data
        except Employee.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response({"msg": "Deleted successfully"}, status=status.HTTP_200_OK)
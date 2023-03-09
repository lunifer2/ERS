from django.urls import path
from .views import EmployeApiView, EmployeeApiIdView

urlpatterns = [
    path('employee/', EmployeApiView.as_view()),
    path('employee/<int:id>/', EmployeeApiIdView.as_view()),

]
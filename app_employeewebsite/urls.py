from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employee_index, name='emp-index'),
    path('employee/show/<int:id>/', views.employee_show, name='emp-show'),
    path('employee/edit/<int:id>/', views.employee_edit, name='emp-edit'),
    path('employee/delete/<int:id>/', views.employee_delete, name='emp-delete'),
    path('employee/add/', views.employee_add, name='emp-add'),
    path('employee/update/', views.employee_update, name='emp-update'),
]
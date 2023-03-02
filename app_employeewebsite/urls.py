from django.urls import path
from . import views 

urlpatterns = [
    path('',views.employee_index,name= 'emp-index'),
    path('employee/',views.employee_index,name='emp-index'),
    path('employee/show/<int:id>/',views.employee_show,name='emp-show'),
    path('employee/add/',views.employee_add,name='emp-add'),
    path('employee/delete/<int:id>',views.employee_delete,name='emp-delete'),
    path('employee/edit/<int:id>',views.employee_edit,name='emp-edit'),
    path('employee/update/',views.employee_update,name='emp-update'),
    path('department/',views.department_index,name='dep-index'),
    path('department/show/<int:id>',views.department_show,name='dep-show'),
    path('department/add/',views.department_add,name='dep-add'),
    path('department/edit/<int:id>',views.department_edit,name='dep-edit'),
    path('department/delete/<int:id>',views.department_delete,name='dep-delete'),
    path('department/update/',views.department_update,name='dep-update'),
    path('salary/',views.salary_record_index,name='salary-index'),
    path('salary/show/<int:id>',views.salary_record_show,name='salary-show'),
    path('salary/add/',views.salary_record_add,name='salary-add'),
    path('salary/edit/<int:id>',views.salary_record_edit,name='salary-edit'),
    path('salary/delete/<int:id>',views.salary_record_delete,name='salary-delete'),
    path('salary/update/',views.salary_record_update,name='salary-update'),
]
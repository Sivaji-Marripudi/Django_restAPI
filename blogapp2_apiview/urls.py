from django.urls import path
from .views import department_list,employee_list,department_detail,employee_detail

urlpatterns = [
    path('departmentapi/',department_list),
    path('emplyeeapi/',employee_list),
    path('departmentapi_detail/<int:pk>/',department_detail),
    path('employeeapi_detail/<int:pk>/',employee_detail)

]

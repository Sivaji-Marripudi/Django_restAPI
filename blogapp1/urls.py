from django.urls import path
from .views import department_list,employee_list
urlpatterns = [
    path('department/',department_list),
    path('employee/',employee_list)
]
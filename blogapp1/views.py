# from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Employee,Department
from rest_framework.parsers import JSONParser
from .serializers import DepartmentSerializer,EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def department_list(request):
    if request.method == 'GET':
        department = Department.objects.all()
        serializer = DepartmentSerializer(department,many = True)
        return JsonResponse(serializer.data,safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DepartmentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 400)

@csrf_exempt      
def employee_list(request):
    if request.method == 'GET':
        data = Employee.objects.all()
        serializer = EmployeeSerializer(data,many= True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EmployeeSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 400)

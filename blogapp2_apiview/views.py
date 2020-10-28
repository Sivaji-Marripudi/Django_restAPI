from django.shortcuts import render
from .models import DepartmentApi,EmployeeApi
from .serializers import DepartmentApiSerializer,EmployeeApiSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET','POST'])
def department_list(request):
    if request.method == 'GET':
        data = DepartmentApi.objects.all()
        serializer = DepartmentApiSerializer(data,many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepartmentApiSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED )
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def department_detail(request,pk):
    try:
        department = DepartmentApi.objects.get(pk = pk)
    except DepartmentApi.DoesNotExist:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = DepartmentApiSerializer(department)
        return Response(data = serializer.data)
    elif request.method == 'PUT':
        serializer = DepartmentApiSerializer(department,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        department.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def employee_list(request):
    if request.method == 'GET':
        data = EmployeeApi.objects.all()
        serializer = EmployeeApiSerializer(data,many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeeApiSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_204_NO_CONTENT)

@api_view(['GET','PUT','DELETE'])
def employee_detail(request,pk):
    try:
        emplyee = EmployeeApi.objects.get(pk = pk)
    except EmployeeApi.DoesNotExist:
        return Response(status= status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        data = EmployeeApiSerializer(emplyee)
        return Response(data.data)
    elif request.method == 'PUT':
        serializer = EmployeeApiSerializer(emplyee,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        emplyee.delete()
        return Response(status = status.HTTP_400_BAD_REQUEST)
        

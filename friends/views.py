from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import City,Friends
from .serializers import CitySerializer,FriendsSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def city_list(request):
    if request.method == 'GET':
        data = City.objects.all()
        serializer = CitySerializer(data,many = True)
        return JsonResponse(serializer.data,safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CitySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 400)


@csrf_exempt
def city_detail(request,pk):
    try:
        city = City.objects.get(pk = pk)
    except City.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method == 'GET':
        serializer = CitySerializer(city)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CitySerializer(city, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status = 400)
    elif request.method == 'DELETE':
        city.delete()
        return HttpResponse(status = 204)

@csrf_exempt
def friends_list(request):
    if request.method == 'GET':
        data = Friends.objects.all()
        serializer = FriendsSerializer(data,many = True)
        return JsonResponse(serializer.data,safe = False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FriendsSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status = 400)
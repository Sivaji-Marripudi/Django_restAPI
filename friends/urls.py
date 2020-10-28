from django.urls import path
from .views import city_list,friends_list,city_detail

urlpatterns = [
    path('city/',city_list),
    path('citydetail/<int:pk>/',city_detail),
    path('friends/',friends_list)
]
from .models import City,Friends
from rest_framework import serializers

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            'city_id',
            'city_name'
        ]

class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = [
            'frnd_id',
            'frnd_name',
            'frnd_email',
            'frnd_dob',
            'frnd_city'
        ]
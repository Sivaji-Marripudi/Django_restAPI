from rest_framework import serializers
from .models import DepartmentApi,EmployeeApi


class DepartmentApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentApi
        fields = [
            'dep_id',
            'dep_name'
        ]

class EmployeeApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeApi
        fields = [
            'emp_id',
            'emp_name',
            'emp_email',
            'emp_date',
            'emp_dep'
        ]
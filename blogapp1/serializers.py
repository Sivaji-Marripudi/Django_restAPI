from rest_framework import serializers
from .models import Employee,Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['dep_id','dep_name','dep_location']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['emp_id','emp_name','emp_email','emp_date','emp_branch']

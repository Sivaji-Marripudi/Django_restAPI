from django.db import models

# Create your models here.

class Department(models.Model):
    dep_id = models.IntegerField(primary_key = True)
    dep_name = models.CharField(max_length = 20)
    dep_location = models.CharField(max_length = 50)

class Employee(models.Model):
    emp_id = models.IntegerField(primary_key = True)
    emp_name = models.CharField(max_length = 100)
    emp_email = models.EmailField()
    emp_date = models.DateTimeField()
    emp_branch = models.ForeignKey(Department,on_delete = models.CASCADE)
    
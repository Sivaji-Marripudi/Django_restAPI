from django.db import models

# Create your models here.
class DepartmentApi(models.Model):
    dep_id = models.AutoField(primary_key = True)
    dep_name = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.dep_id) + '-' + self.dep_name
class EmployeeApi(models.Model):
    emp_id = models.AutoField(primary_key = True)
    emp_name = models.CharField(max_length = 50)
    emp_email = models.EmailField()
    emp_date = models.DateField()
    emp_dep = models.ForeignKey(DepartmentApi,on_delete = models.CASCADE)

    def __str__(self):
        return self.emp_name
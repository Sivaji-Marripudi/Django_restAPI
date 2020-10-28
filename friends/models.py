from django.db import models

# Create your models here.
class City(models.Model):
    city_id = models.IntegerField(primary_key = True)
    city_name = models.CharField(max_length = 50)
    dist = models.CharField(max_length = 30)
    def __str__(self):
        
        return str(self.city_id) + '-' + self.city_name 

class Friends(models.Model):
    frnd_id = models.IntegerField(primary_key = True)
    frnd_name = models.CharField(max_length = 50)
    frnd_email = models.EmailField()
    frnd_dob = models.DateField()
    frnd_city = models.ForeignKey(City,on_delete = models.CASCADE)

    def __str__(self):
        return str(self.frnd_id) + '-' + self.frnd_name

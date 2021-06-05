from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER_SELECTION = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Specified'),
]


class CustomUser(AbstractUser):
    age = models.IntegerField(blank=True,null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    height = models.IntegerField(blank=True,null=True)
    weight = models.IntegerField(blank=True,null=True)
    



class Measurements(models.Model):
    systolic = models.IntegerField()
    diastolic  = models.IntegerField()
    pulse = models.IntegerField()
    measurement_date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.measurement_date
    
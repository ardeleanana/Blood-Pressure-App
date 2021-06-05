from django.contrib import admin
from .models import  CustomUser, Measurements


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Measurements)
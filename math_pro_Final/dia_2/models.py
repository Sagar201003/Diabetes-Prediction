from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.http import request
from django.db import models
from django.contrib import messages
# # Create your models here.
class Peopleinfo(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False,unique=False)
    preg=models.FloatField(unique=False)
    glu=models.FloatField(unique=False) 
    # Phone=models.CharField(max_length=10,unique=False)
    bp=models.FloatField(unique=False) 
    insulin=models.FloatField(unique=False)
    height=models.FloatField(unique=False)
    weight=models.FloatField(unique=False)
    dpf=models.FloatField(unique=False)
    age=models.FloatField(unique=False)
    gender=models.FloatField(unique=False)

# Create your models here.

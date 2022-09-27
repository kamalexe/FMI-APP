from django.db import models
from datetime import datetime

# Create your models here.
class SmUser(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=20 ,unique=True)
    password = models.CharField(max_length=20)
    bdate = models.DateTimeField(max_length=20)
    gender = models.CharField(max_length=20)
    creatDate = models.DateTimeField(default=datetime.now(), blank=True)
    updateDate = models.DateTimeField(default=datetime.now(), blank=True)

class SmUserProfile(models.Model):
    user_id = models.CharField(max_length=20)
    fname = models.CharField(max_length=20 ,default='Ferb')
    lname = models.CharField(max_length=20,default='Fletcher')
    email = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20,blank=True)
    bdate = models.DateTimeField(max_length=20,blank=True)
    gender = models.CharField(max_length=20,blank=True)
    city = models.CharField(max_length=20,blank=True)
    userType = models.CharField(max_length=20 ,blank=True)
    about = models.TextField(blank=True)
    creatDate = models.DateTimeField(default=datetime.now(), blank=True)
    updateDate = models.DateTimeField(default=datetime.now(), blank=True)
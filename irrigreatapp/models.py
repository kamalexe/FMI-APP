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
    creatDate = models.DateTimeField( blank=True)
    updateDate = models.DateTimeField( blank=True)

class SmUserProfile(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
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
    image = models.ImageField(upload_to = 'irrigreatapp/images',default='irrigreatapp/images/defaultimg.png')
    follow = models.ManyToManyField(SmUser, related_name='follower')
    creatDate = models.DateTimeField( blank=True)
    updateDate = models.DateTimeField( blank=True)

    def total_follow(self):
        return self.follow.count()
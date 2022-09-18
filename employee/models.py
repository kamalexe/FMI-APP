from django.db import models

# Create your models here.
# Create your models here.
class Employee(models.Model):
    empid = models.CharField(max_length=20,primary_key=True)
    empname = models.CharField(max_length=50)
    address = models.TextField()
    # max length of TextFiel() is 225
    depertment = models.CharField(max_length=50)
    salary = models.FloatField()
from django.db import models
from fmiapp.models import FarmerInfo
from merchantapp.models import orderDetail
from datetime import datetime

# Create your models here.
class Profile(models.Model):
    farmerName = models.OneToOneField(FarmerInfo,on_delete = models.CASCADE, default="")

class FarmerSellProduct(models.Model):
    farmerName = models.ForeignKey(FarmerInfo,on_delete = models.CASCADE , default="")
    productName = models.CharField(max_length=100, default="")
    qty = models.CharField(max_length=100, default="")
    price = models.CharField(max_length=100, default="")
    # profile = models.ForeignKey(Profile,on_delete = models.CASCADE, default="")
    def __str__(self):
        return self.productName

class Tracker(models.Model):
    orderId = models.CharField(max_length=100, default="")
    orderStatus = models.CharField(max_length=100, default="Your Order has been placed")
    updateDate = models.DateTimeField(default=datetime.now(), blank=True)
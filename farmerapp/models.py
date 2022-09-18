from django.db import models
from fmiapp.models import FarmerInfo

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

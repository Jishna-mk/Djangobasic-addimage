from django.db import models
from email.policy import default
from unittest.util import _MAX_LENGTH

# Create your models here.
class Productlist(models.Model):
    Product_ID=models.AutoField(primary_key=True)
    Product_name=models.CharField(max_length=200)
    Product_category=models.CharField(max_length=200)
    Product_price=models.CharField(max_length=200)
    Product_image=models.ImageField(null=True ,blank=True,upload_to="products")

from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    status = models.CharField(max_length=100)
    image= models.CharField(max_length=2560)

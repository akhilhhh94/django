from django.db import models
from django.db.models.base import Model

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    status = models.CharField(max_length=100)
    image= models.FileField(upload_to="documents")


class Subscription(models.Model):
    email = models.EmailField(max_length = 254, null=False, blank=False, unique=True)

    def __str__(self):
        return self.email

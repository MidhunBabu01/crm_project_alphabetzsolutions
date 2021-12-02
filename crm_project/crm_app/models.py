from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=250)
    
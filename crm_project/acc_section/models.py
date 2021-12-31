from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExtendedUserModel(models.Model):
    def __str__(self):
        return self.user.username
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    comapny_name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    company_address = models.TextField()
    dob = models.CharField(max_length=10)
    gst = models.IntegerField()
    phn_number = models.CharField(max_length=13)
    age = models.IntegerField()
    
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExtendedUserModel(models.Model):
    def __str__(self):
        return self.user.username
    phn_number = models.CharField(max_length=13)
    age = models.IntegerField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)
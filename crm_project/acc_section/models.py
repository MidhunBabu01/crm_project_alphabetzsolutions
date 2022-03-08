from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ExtendedUserModel(models.Model):
    def __str__(self):
        return self.user.username
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    employe_name = models.CharField(max_length=25)
    address = models.TextField()
    dob = models.DateField()
    blood_group = models.CharField(max_length=5)
    phn_number = models.IntegerField(max_length=10)
    is_staff2= models.CharField(max_length=10,blank=True,null=True)
    is_superviser = models.CharField(max_length=10,blank=True,null=True)
    user_photo = models.ImageField(upload_to = 'pictures',blank=True,null=True)
    # is_employee = models.BooleanField('Is employee', default=False)
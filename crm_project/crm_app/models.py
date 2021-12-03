from django.db import models

# Create your models here.
class Customer(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    image = models.ImageField(upload_to="pictures")
    loaction = models.CharField(max_length=50)
    category_choices = (
        ("test1", "test1"),
        ("test2", "test3"),
    )
    gst = models.CharField(max_length=50,blank=True)
    category = models.CharField(choices=category_choices,max_length=100,default='1')
    whatsapp_number = models.CharField(max_length=10)

    
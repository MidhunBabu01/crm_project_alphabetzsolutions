from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Tools_item(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=250)


class CartListt(models.Model):
    cart_id = models.CharField(max_length=50,unique=True)
    Date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id

class Itemss(models.Model):
    # def __str__(self):
    #     return self.prodt.product_name
    prodt = models.ForeignKey(Tools_item,on_delete=models.CASCADE,blank=True,null=True)
    cart = models.ForeignKey(CartListt,on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    active = models.BooleanField(default=True,blank=True,null=True)
    order_Date = models.DateTimeField(default=datetime.now(),blank=True,null=True)
    # due_date = models.DateTimeField(default=datetime.now() + timedelta(days=30),blank=True,null=True) 
    # @property
    # def total(self):
    #     gst = (self.prodt.price*self.quantity*self.prodt.gst)/100
    #     return self.prodt.price*self.quantity+gst

from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Tools_item(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=250)




class CartList(models.Model):
    cart_id = models.CharField(max_length=50,unique=True)
    Date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id

class Items(models.Model):
    # def __str__(self):
    #     return self.prodt.product_name
    prodt = models.ForeignKey(Tools_item,on_delete=models.CASCADE)
    cart = models.ForeignKey(CartList,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    order_Date = models.DateTimeField(default=datetime.now())
    due_date = models.DateTimeField(default=datetime.now() + timedelta(days=30)) 
    # @property
    # def total(self):
    #     gst = (self.prodt.price*self.quantity*self.prodt.gst)/100
    #     return self.prodt.price*self.quantity+gst

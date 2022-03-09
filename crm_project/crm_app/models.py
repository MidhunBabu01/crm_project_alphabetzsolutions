from django.db import models
from django.db.models.fields import CharField
from django.forms.fields import DateTimeField
# import datetime
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from multiselectfield import MultiSelectField


# Create your models here.
class Customer(models.Model):
    def __str__(self):
        return self.name
    staff_name = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    image = models.ImageField(upload_to="pictures")
    loaction = models.CharField(max_length=50)
    state = models.CharField(max_length=10,default='Kerala',blank=True,null=True)
    category_choices = (
        ("Person", "Person"),
        ("Contractor", "Contractor"),
        ("Company", "Company"),
    )
    gst = models.CharField(max_length=50,blank=True)
    category = models.CharField(choices=category_choices,max_length=100,default='1')
    whatsapp_number = models.CharField(max_length=10)
    last_transaction = models.CharField(max_length=250,blank=True)
    total_transaction = models.CharField(max_length=250,blank=True)


# class Tools(models.Model):
#     def __str__(self):
#         return self.name
#     name = models.CharField(max_length=25)

class Leads(models.Model):
    def __str__(self):
        return self.company_name
    staff_name = models.ForeignKey(User,on_delete=models.CASCADE)
    no = models.IntegerField()
    date = models.DateField(default=datetime.now())
    company_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone1 = models.CharField(max_length=10)
    phone2 = models.CharField(max_length=10)
    owner = models.CharField(max_length=250)
    choice = (
        ('IT','IT'),
        ('NON IT','NON IT')
    )
    department = models.CharField(max_length=10,choices=choice)
    requirements = models.CharField(max_length=250)
    remarks = models.CharField(max_length=250)
    stage1 = models.CharField(max_length=250)
    stage2 = models.CharField(max_length=250)
    lead_choices = (
        ('pending leads','pending leads'),
        ('open leads','open leads'),
        ('close leads','close leads')
    )
    lead_status = models.CharField(max_length=25,choices=lead_choices)
    source_choices = (
        ('Facebook','Facebook'),
        ('Youtube','Youtube'),
        ('Website','Website'),
        ('Newspaper','Newspaper'),
    )
    lead_source = models.CharField(max_length=25,choices=source_choices)
    # PROJECT MANAGEMENT SECTION
    status_choices = (
        ('Pending','Pending'),
        ('Started','Started'),
        ('On Hold','On Hold'),
        ('End','End')
    )
    status = models.CharField(max_length=25,choices=status_choices,blank=True,null=True,default='Pending')
    start_date = models.CharField(max_length=10,blank=True,null=True)
    end_date = models.CharField(max_length=10,blank=True,null=True)
    tools = models.CharField(max_length=250,blank=True,null=True)
    Return = models.CharField(max_length = 250,blank=True,null=True)
    start_date2 = models.CharField(max_length=10,blank=True,null=True)
    end_date2 = models.CharField(max_length=10,blank=True,null=True)
    site_staff_name = models.ForeignKey(User,on_delete=models.CASCADE,related_name="site_staff_name",blank=True,null=True)



class Quotation(models.Model):
    prodt_rate = models.IntegerField()
    gst = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='pictures')


class Quotation_Invoice(models.Model):
    def __str__(self):
        return self.company_name()
    # invoice
    choice = (
        ('Alphabet Solutionz','Alphabet Solutionz'),
        ('Alphabet Technologies','Alphabet Technologies')
    )
    company_name = models.CharField(max_length=250,choices=choice,default='1')
    company_address = models.TextField(max_length=250)
    # billing
    customer_name = models.CharField(max_length=250)
    customer_address = models.CharField(max_length=250)
    date = models.DateField()
    due_date = models.DateField()
    item_name = models.CharField(max_length=250)
    item_code = models.CharField(max_length=250)
    quantity = models.IntegerField()
    rate = models.IntegerField()
    UOM = models.CharField(max_length=250)
    warranty = models.CharField(max_length=250)
    hsn_code = models.CharField(max_length=250)
    gst_choices = (
        ('5%','5%'),
        ('12%','12%'),
        ('18%','18%'),
        ('28%','28%')
    )
    gst = models.CharField(max_length=250,choices=gst_choices)
    notes = models.CharField(max_length=250)
    terms_and_conditions = models.CharField(max_length=250)



class Product_Categoryy(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Products(models.Model):
    def __str__(self):
        return self.product_name

    # slug = models.SlugField(max_length=250) 
    category = models.ForeignKey(Product_Categoryy,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250)
    brand = models.CharField(max_length=25,blank=True)
    photo = models.ImageField(upload_to ='products')
    # desc = models.TextField()
    hsn = models.CharField(max_length=25,blank=True,null=True)
    price = models.IntegerField()
    warranty = models.CharField(max_length=250,blank=True,null=True)
    item_code = models.CharField(max_length=25,blank=True,null=True)
    uom = models.CharField(max_length=25,blank=True,null=True)
    gst1 = 5
    gst2 = 12
    gst3 = 18
    gst4 = 28
    gst_choice = (
        (gst1,'5'),
        (gst2,'12'),
        (gst3,'18'),
        (gst4,'28')
    )
    gst = models.IntegerField(choices=gst_choice)
    stock = models.IntegerField()
    



# CART SECTIONS

class CartList(models.Model):
    cart_id = models.CharField(max_length=50,unique=True)
    Date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.cart_id

class Items(models.Model):
    def __str__(self):
        return self.prodt.product_name

    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    prodt = models.ForeignKey(Products,on_delete=models.CASCADE)
    cart = models.ForeignKey(CartList,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    order_Date = models.DateTimeField(default=datetime.now())
    due_date = models.DateTimeField(default=datetime.now() + timedelta(days=30))
    @property
    def invoice_number(self):
        return self.prodt.id + 5000
    
    @property
    def total(self):
        gst = (self.prodt.price*self.quantity*self.prodt.gst)/100
        return self.prodt.price*self.quantity+gst




class Quotation_Details(models.Model):
    def __str__(self):
        return self.quotation_details.name
    quotation_details = models.ForeignKey(Customer,on_delete=models.CASCADE)





class Task(models.Model):
    task_owner = models.CharField(max_length=25)
    subjects = models.CharField(max_length=50)
    due_date = models.DateField()
    status_choices = (
        ('Not Stared','Not Started'),
        ('Deferred','Deferred'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
        ('Waiting For Approval','Waiting For Approval'),
    )
    status = models.CharField(choices=status_choices,max_length=50)
    priority_choices = (
        ('High','High'),
        ('Highest','Highest'),
        ('Low','Low'),
        ('Lowest','Lowest')
    )
    priority = models.CharField(choices=priority_choices,max_length=50)
    desc = models.TextField(blank=True,null=True)

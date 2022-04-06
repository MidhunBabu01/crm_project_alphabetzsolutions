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
    staff_name = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=250,blank=False,null=False)
    address = models.CharField(max_length=250,blank=False,null=False)
    phone = models.CharField(max_length=10,blank=False,null=False)
    email = models.EmailField(blank=True,null=True)
    image = models.ImageField(upload_to="pictures",blank=True,null=True)
    loaction = models.CharField(max_length=50,blank=False,null=False)
    state = models.CharField(max_length=10,default='Kerala',blank=False,null=False)
    category_choices = (
        ("Person", "Person"),
        ("Contractor", "Contractor"),
        ("Company", "Company"),
    )
    gst = models.CharField(max_length=50,blank=True,null=True)
    category = models.CharField(choices=category_choices,max_length=100,default='1')
    whatsapp_number = models.CharField(max_length=10,blank=True,null=True)
    last_transaction = models.CharField(max_length=250,blank=True,null=True)
    total_transaction = models.CharField(max_length=250,blank=True,null=True)


# class Tools(models.Model):
#     def __str__(self):
#         return self.name
#     name = models.CharField(max_length=25)

class Leads(models.Model):
    def __str__(self):
        return self.company_name
    staff_name = models.ForeignKey(User,on_delete=models.CASCADE)
    no = models.IntegerField(blank=False,null=False)
    date = models.DateField(default=datetime.now(),blank=False, null=False)
    company_name = models.CharField(max_length=250,blank=True, null=True)
    address = models.CharField(max_length=250,blank=False, null=False)
    phone1 = models.CharField(max_length=10,blank=False, null=False)
    phone2 = models.CharField(max_length=10,blank=False, null=False)
    owner = models.CharField(max_length=250,blank=False, null=False)
    choice = (
        ('IT','IT'),
        ('NON IT','NON IT')
    )
    department = models.CharField(max_length=10,choices=choice,blank=False, null=False)
    requirements = models.CharField(max_length=250,blank=False, null=False)
    remarks = models.CharField(max_length=250,blank=True, null=True)
    stage1 = models.CharField(max_length=250,blank=True, null=True)
    stage2 = models.CharField(max_length=250,blank=True, null=True)
    lead_choices = ( 
        ('pending leads','pending leads'),
        ('open leads','open leads'),
        ('close leads','close leads')
    )
    lead_status = models.CharField(max_length=25,choices=lead_choices,blank=False, null=False)
    source_choices = (
        ('Facebook','Facebook'),
        ('Youtube','Youtube'),
        ('Website','Website'),
        ('Newspaper','Newspaper'),
    )
    lead_source = models.CharField(max_length=25,choices=source_choices,blank=False,null=False)
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

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,max_length=25, blank=True,null=True)
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
    def __str__(self):
        return self.staff_name.username
        
    staff_name = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    subjects = models.CharField(max_length=50,blank=True,null=True)
    due_date = models.DateField(blank=True,null=True)
    status_choices = ( 
        ('Not Started','Not Started'),
        ('Deferred','Deferred'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
        ('Waiting For Approval','Waiting For Approval'),
    )
    status = models.CharField(choices=status_choices,max_length=50,blank=True,null=True)
    priority_choices = (
        ('High','High'),
        ('Highest','Highest'),
        ('Low','Low'),
        ('Lowest','Lowest'),
    )
    priority = models.CharField(choices=priority_choices,max_length=50,blank=True,null=True)
    desc = models.TextField(blank=True,null=True)

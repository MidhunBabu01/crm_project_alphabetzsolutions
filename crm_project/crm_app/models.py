from django.db import models
from django.db.models.fields import CharField
from django.forms.fields import DateTimeField
import datetime

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
        ("Person", "Person"),
        ("Contractor", "Contractor"),
        ("Company", "Company"),
    )
    gst = models.CharField(max_length=50,blank=True)
    category = models.CharField(choices=category_choices,max_length=100,default='1')
    whatsapp_number = models.CharField(max_length=10)
    last_transaction = models.CharField(max_length=250,blank=True)
    total_transaction = models.CharField(max_length=250,blank=True)






    

class Leads(models.Model):
    def __str__(self):
        return self.company_name
    no = models.IntegerField()
    date = models.DateField(default=datetime.date.today)
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
        ('junk_leads','junk_leads'),
        ('open_leads','open_leads'),
        ('close_leads','close_leads')
    )
    lead_status = models.CharField(max_length=25,choices=lead_choices)




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
    qty = models.IntegerField()
    rate = models.IntegerField()
    amount = models.IntegerField()
    gst = models.BooleanField(default=False)
    notes = models.CharField(max_length=250)
    terms_and_conditions = models.CharField(max_length=250)




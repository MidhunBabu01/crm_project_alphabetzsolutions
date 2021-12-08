from django.contrib import admin
from .models import Customer,Leads,Quotation_Invoice
# Register your models here.
admin.site.register(Customer)
admin.site.register(Leads)
admin.site.register(Quotation_Invoice)
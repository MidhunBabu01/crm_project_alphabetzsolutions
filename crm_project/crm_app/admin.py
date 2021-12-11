from django.contrib import admin
from .models import Customer,Leads,Quotation_Invoice,Products,Items,CartList
# Register your models here.
admin.site.register(Customer)
admin.site.register(Leads)
admin.site.register(Quotation_Invoice)
admin.site.register(Products)
admin.site.register(CartList)
admin.site.register(Items)


class AdminProducts(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
from django.contrib import admin
from .models import Customer,Leads,Products,Items,CartList,Quotation_Details
# Register your models here.
admin.site.register(Customer)
admin.site.register(Leads)
admin.site.register(Products)
admin.site.register(CartList)
admin.site.register(Items)
admin.site.register(Quotation_Details)


class AdminProducts(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
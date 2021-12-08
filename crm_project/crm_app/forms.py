from django.forms import widgets
from.models import Customer, Leads, Quotation_Invoice
from django import forms
from flatpickr import DatePickerInput




class CustomerAddForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['last_transaction','total_transaction']
        widgets ={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'photo' : forms.TextInput(attrs={'class':'form-control-file'}),
            'loaction' : forms.TextInput(attrs={'class':'form-control'}),
            'gst' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
            'whatsapp_number' : forms.TextInput(attrs={'class':'form-control'}),
            
        }




class LeadAddForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = '__all__'
        widgets ={
            'no' : forms.TextInput(attrs={'class':'form-control'}),
            'date' : DatePickerInput(attrs={'class':'form-control'}),
            'company_name' : forms.TextInput(attrs={'class':'form-control'}),
            'phone1' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'phone2' : forms.TextInput(attrs={'class':'form-control'}),
            'owner' : forms.TextInput(attrs={'class':'form-control'}),
            'department' : forms.Select(attrs={'class':'form-control'}),
            'requirements' : forms.TextInput(attrs={'class':'form-control'}),
            'remarks' : forms.TextInput(attrs={'class':'form-control'}),
            'stage1' : forms.TextInput(attrs={'class':'form-control'}),
            'stage2' : forms.TextInput(attrs={'class':'form-control'}),
            'lead_status' : forms.Select(attrs={'class':'form-control'}),
        }





class Quotation_invoice_form(forms.ModelForm):
    class Meta:
        model = Quotation_Invoice
        fields = '__all__'
        widgets = {
            'company_name' : forms.TextInput(attrs={'placeholder':'company name'}),
            'company_address' : forms.TextInput(attrs={'placeholder':'company address'}),
            'customer_name' : forms.TextInput(attrs={'placeholder':'customer name'}),
            'customer_address' : forms.TextInput(attrs={'placeholder':'customer address'}),
            'item_name' : forms.TextInput(attrs={'placeholder':'add item'}),
            'qty': forms.TextInput(attrs={'placeholder':'qty'}),
            'rate': forms.TextInput(attrs={'placeholder':'rate'}),
            'amount': forms.TextInput(attrs={'placeholder':'amount'}),
            'notes': forms.TextInput(),
            'terms_and_conditions': forms.TextInput()
        }

from django_select2.forms import Select2MultipleWidget
from django.forms import CheckboxSelectMultiple, widgets
from.models import Customer, Leads, Quotation_Details, Task
from django import forms
from flatpickr import DatePickerInput




class CustomerAddForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['last_transaction','total_transaction','staff_name']
        widgets ={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.NumberInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            # 'image' : forms.ImageField(),
            'loaction' : forms.TextInput(attrs={'class':'form-control'}),
            'gst' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
            'state' : forms.TextInput(attrs={'class':'form-control'}),
            'whatsapp_number' : forms.NumberInput(attrs={'class':'form-control'}),
            
        }




class LeadAddForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = '__all__'
        exclude = ['staff_name','status','start_date','end_date','tools','Return','start_date2','end_date2','site_staff_name']
        widgets ={
            'no' : forms.TextInput(attrs={'class':'form-control'}),
            'date' : DatePickerInput(attrs={'class':'form-control','type':'date'}),
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
            'lead_source' : forms.Select(attrs={'class':'form-control'})
        }   


class ProjectManagementAddForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = ['status','start_date','end_date']
        # exclude = ['lead_source','lead_status','stage2','stage1','remarks','requirements','department','owner','phone2','address','phone1','staff_name','no','date','company_name','lead_status','lead_source','stage1','stage2']
        widgets ={
            'status' : forms.Select(attrs={'class':'form-control'}),
            'start_date' : forms.TextInput(attrs={'class':'form-control','placeholder':'DD/MM/YY'}),
            'end_date' : forms.TextInput(attrs={'class':'form-control','placeholder':'DD/MM/YY'}),
            
        }   

class ToolsManagementUpdate(forms.ModelForm):
    class Meta:
        model = Leads
        fields = ['start_date2','end_date2']
        labels ={
            'retur_n':'Return',
            'start_date2':'Start Date',
            'end_date2': 'End Date'
        }
        CHOICES = (
            ("Cable","Cable"), 
            ("Driller","Driller"),
            ('Screw','Screw'),
            ('Screwdriver','Screwdriver'),
            ('Nut','Nut'),
            ('Hammer','Hammer'),
            ('Mallet','Mallet'),
            ('Wrench','Wrench'),
        )

        widgets ={
            'Return' : forms.CheckboxSelectMultiple(choices=CHOICES,attrs={}),
            'start_date2' : forms.TextInput(attrs={'class':'form-control','placeholder':'DD/MM/YY'}),
            'end_date2' : forms.TextInput(attrs={'class':'form-control','placeholder':'DD/MM/YY'}),
            'tools' : forms.CheckboxSelectMultiple(choices=CHOICES,attrs={})
            # 'site_staff' : forms.TextInput(attrs={'class':'form-control'}),
        }  
    # CHOICES = (
    #     ("Cable","Cable"), 
    #     ("Driller","Driller"),
    #     ('Screw','Screw'),
    #     ('Screwdriver','Screwdriver'),
    #     ('Nut','Nut'),
    #     ('Hammer','Hammer'),
    #     ('Mallet','Mallet'),
    #     ('Wrench','Wrench'),
    # )
    # tools=forms.MultipleChoiceField(choices=CHOICES,required=False,widget=forms.CheckboxSelectMultiple(attrs={}))
    # Return=forms.MultipleChoiceField(choices=CHOICES,required=False,widget=forms.CheckboxSelectMultiple(attrs={}))
    




class Quotation_DetailsForm(forms.ModelForm):
    class Meta:
        model = Quotation_Details
        fields = '__all__'
        labels = {
            'quotation_details':'Customer Name'
        }
        widgets ={
            'quotation_details': forms.Select(attrs={'class':'form-control'})

        }


class TaskAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'staff_name' : forms.Select(attrs={'class':'form-control'}),
            'subjects': forms.TextInput(attrs={'class':'form-control'}),
            'due_date' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'status' : forms.Select(attrs={'class':'form-control'}),
            'priority' : forms.Select(attrs={'class':'form-control'}),
            'desc' : forms.Textarea(attrs={'rows':'3','class':'form-control'}),

        }


class StaffTaskAddForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['staff_name','subjects','due_date','priority','desc']
        widgets = {
            'status' : forms.Select(attrs={'class':'form-control'}),

        }






# class Quotation_invoice_form(forms.ModelForm):
#     class Meta:
#         model = Quotation_Invoice
#         fields = '__all__'
#         widgets = {
#             'company_name' : forms.Select(attrs={'class':'form-control'}),
#             'company_address' : forms.Textarea(attrs={'placeholder':'company address'}),
#             'customer_name' : forms.TextInput(attrs={'placeholder':'customer name'}),
#             'customer_address' : forms.TextInput(attrs={'placeholder':'customer address'}),
#             'item_name' : forms.TextInput(attrs={"class":"item"}),
#             'quantity': forms.NumberInput(attrs={'class':'quantity'}),
#             'rate': forms.NumberInput(attrs={'class':'rate'}),
#             'item_code': forms.TextInput(attrs={'class':'item_code'}),
#             'gst': forms.Select(attrs={'class':'form-control '}),
#             'UOM': forms.TextInput(attrs={'class':'uom'}),
#             'warranty': forms.TextInput(attrs={'class':'warranty'}),
#             'hsn_code': forms.TextInput(attrs={'class':'hsn'}),
#             'notes': forms.TextInput(),
#             'terms_and_conditions': forms.TextInput()
#         }







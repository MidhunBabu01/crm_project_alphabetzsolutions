from.models import Customer
from django import forms




class CustomerAddForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets ={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            # 'photo' : forms.TextInput(attrs={'class':'form-control'}),
            'loaction' : forms.TextInput(attrs={'class':'form-control'}),
            'gst' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(attrs={'class':'form-control'}),
            'whatsapp_number' : forms.TextInput(attrs={'class':'form-control'}),
            
        }
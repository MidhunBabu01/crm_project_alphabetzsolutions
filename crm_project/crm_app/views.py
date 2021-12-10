from django.core.exceptions import RequestAborted
from django.shortcuts import redirect, render
from .models import Customer, Leads, Products
from .forms import CustomerAddForm,LeadAddForm,Quotation_invoice_form


# Create your views here.
def index(request):
    return render(request,'index.html')


def chat(request):
    return render(request,'chat.html')


def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('userpassword')
        if username == 'Midhun' and password=='123':
            return redirect('crm_app:leads')
        else:
            return redirect('crm_app:login')
    return render(request,'login.html')

def register(request):
    return render(request,"register.html")


def starter(request):
    return render(request,'pages-starter.html')



def customer(request):
    customer = Customer.objects.all() 
    return render(request,"customer.html",{'customer':customer})

def add_customer(request):
    form = CustomerAddForm()
    if request.method == 'POST':
        form = CustomerAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crm_app:customers')
    else:
        form = CustomerAddForm()
    return render(request,'addcustomer.html',{'form':form})


def leads(request):
    leads = Leads.objects.all()
    return render(request,"leads.html",{'leads':leads})

def add_leads(request):
    fm = LeadAddForm()
    if request.method == 'POST':
        fm = LeadAddForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('crm_app:leads')
    else:
        fm = LeadAddForm()
    return render(request,'add_leads.html',{'form':fm})




def junk_leads(request):
    junk_leads = Leads.objects.filter(lead_status='junk_leads')
    return render(request,'junk_leads.html',{'junk_leads':junk_leads})


def open_leads(request):
    open_leads = Leads.objects.filter(lead_status="open_leads")
    return render(request,'open_leads.html',{'open_leads':open_leads})

def closed_leads(request):
    closed_leads = Leads.objects.filter(lead_status="close_leads")
    return render(request,'closed_leads.html',{'close_leads':closed_leads})


def customer_profile(request,customer_id):
    customer_profile= Customer.objects.filter(id=customer_id)
    return render(request,'user_profile.html',{'customer_profile':customer_profile})


def Quotation_invoice(request):
    details = {
        'company_address':'TC 13/1113 Thopil LineMedical College PO, Kumarapuram -695011Trivandrum, Kerala'
        }
    forms = Quotation_invoice_form(initial=details)
    return render(request,"quotation_invoice.html",{'forms':forms})



def products(request):
    products = Products.objects.all()
    return render(request,'products.html',{'products':products})


from django.core.exceptions import ObjectDoesNotExist, RequestAborted
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from .models import Customer, Leads, Products,CartList,Items
from .forms import CustomerAddForm,LeadAddForm,Quotation_invoice_form
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


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

def cart(request,total=0,count=0,cart_items=None):
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
        ct_items = Items.objects.filter(cart=ct,active=True) 
        for i in ct_items:
            total +=(i.prodt.price*i.quantity)
            count += i.quantity      
    except ObjectDoesNotExist:
        return redirect("crm_app:cart2")
    return render(request,"cart.html",{"ct_items":ct_items, "total":total, "count":count})


def cart2(request):
    return render(request,'cart2.html') 

def c_id(request):
    carttt_id = request.session.session_key
    if not carttt_id:
        carttt_id = request.session.create()
    return carttt_id


def add_cart(request,product_id):
    product = Products.objects.get(id=product_id)
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
    except CartList.DoesNotExist:
        ct = CartList.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items = Items.objects.get(prodt=product,cart=ct)
        if c_items.quantity < c_items.prodt.stock:
            c_items.quantity+=1
        c_items.save()
    except Items.DoesNotExist:
        c_items =Items.objects.create(prodt=product,quantity=1,cart=ct)
        c_items.save()
    return redirect("crm_app:addcart")




def minus_button(request, product_id):
    ct = CartList.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Products,id=product_id)
    c_items = Items.objects.get(prodt=prod, cart=ct)
    if c_items.quantity>1:
        c_items.quantity-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect("crm_app:addcart")



def delete_button(request,product_id):
    ct = CartList.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Products,id=product_id)
    c_items = Items.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect("crm_app:addcart")




def count(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct = CartList.objects.filter(cart_id=c_id(request))
            cti = Items.objects.all().filter(cart=ct)
            for c in cti:
                item_count+=c.quantity
        except CartList.DoesNotExist:
            item_count = 0
        return render({"count":item_count})     


def cart_delete(request):
    return render(request,'cart2.html')




def search(request):
    product = None
    Query = None
    if 'q' in request.GET:
        Query = request.GET.get('q')
        product = Products.objects.all().filter(Q(product_name__icontains=Query)|Q(hsn__icontains=Query))
    return render(request,'search_result.html',{"product":product,"query":Query})
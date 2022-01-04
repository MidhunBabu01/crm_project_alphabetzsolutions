from django.core.exceptions import ObjectDoesNotExist, RequestAborted
from django.http.response import HttpResponse, ResponseHeaders
from django.shortcuts import redirect, render,get_object_or_404
from crm_app.models import Customer, Leads, Products,CartList,Items
from .forms import CustomerAddForm, LeadAddForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.db.models import Q
from acc_section.models import ExtendedUserModel
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.
def index(request):
    return render(request,'index.html')


def chat(request):
    return render(request,'chat.html')




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



def lead_update(request,item_id):
    if request.method == 'POST':
        update  = Leads.objects.get(id=item_id)
        fm = LeadAddForm(request.POST,instance=update)
        if fm.is_valid():
            fm.save()
            return redirect("crm_app:leads")
    else:
        update  = Leads.objects.get(id=item_id)
        fm = LeadAddForm(instance=update)
    return render(request,"lead_edit.html",{'form':fm})


def lead_delete(request,item_id):
    obj = Leads.objects.filter(id=item_id)
    obj.delete()
    return redirect('crm_app:leads')




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

# @login_required
def Quotation_invoice(request,cart_items=None,total=0,count=0):
    # Usertable.filter(extendedtable__address)
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
        ct_items = Items.objects.filter(cart=ct,active=True) 
        for i in ct_items:
            total += i.total
            count += i.quantity
    except ObjectDoesNotExist:
        return redirect("crm_app:cart2")
    return render(request,"quotation_invoice.html",{"ct_items":ct_items, "total":total, "count":count})


@login_required
def products(request):
    products = Products.objects.all()
    return render(request,'products.html',{'products':products})

def cart(request,total=0,count=0,cart_items=None):
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
        ct_items = Items.objects.filter(cart=ct,active=True) 
        for i in ct_items:
            total += i.total
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
    return redirect("crm_app:products")



def buy_now(request,product_id):
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




# ACCOUNT_SECTION
# CUSTOMER ACCOUNT SECTION
def register(request):
    if "username" in request.session:
        return redirect('crm_app:index')
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                print('username already taken')
                return render(request,'register.html',{'error':"username alredy taken"})
                
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password'],first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'])
                phn = request.POST['phn']
                age = request.POST['age']
                company_name = request.POST['company_name']
                company_address = request.POST['company_address']
                title = request.POST['title']
                dob = request.POST['dob']
                gst = request.POST['gst']
                extenduser = ExtendedUserModel(phn_number=phn,age=age,user=user,comapny_name=company_name,company_address=company_address,title=title,gst=gst,dob=dob)
                extenduser.save();
                print('user created')
                auth.login(request,user)
                return redirect('crm_app:login')
        else:
            print('password not matching')
            return render(request,'register.html',{'error':'password doesnot match'})
    else:
        return render(request,'register.html')



def login(request):
    if 'username' in request.session:
        return redirect('crm_app:index')
    if request.method=='POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            request.session['username'] = request.POST['username']
            auth.login(request,user)
            print("logged in")
            return JsonResponse(
                {'success':True},
                safe=False
            )
            # return redirect('crm_app:index') 
        else:
            auth.login
            return JsonResponse(
                {'success':False},
                safe=False
            )
            # return render(request,'login.html',{'error':'Invlaid login credentials'})
    else:
        return render(request,'login.html')




# def register(request):
#     if "username" in request.session:
#         return redirect('crm_app:index')
#     if request.method == "POST":
#         firstname = request.POST.get("first_name")
#         lastname = request.POST.get("last_name")
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password1 = request.POST.get("password1")
#         password2 = request.POST.get("password2")  
#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 print("username alredy exists")
#                 messages.info(request,"username already exist")
#                 return redirect("crm_app:register")
#             elif User.objects.filter(email=email).exists():
#                 print("email alredy exists")
#                 messages.info(request,"email  already registered")
#                 return redirect("crm_app:register")
#             else:
#                 user = User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password1)
#                 user.save();
#                 print('user created')
#                 return redirect('crm_app:login')
#         else:
#             print('Password Not Matched')
#             return redirect('crm_app:register')    
#     return render(request,"register.html")



# def customer_address(request):
#     form = 
#     if request.method == 'POST':
#         form = (request.POST)
#         if form.is_valid():
#             form.save();
#             print('address created')
#             return redirect('crm_app:login')
#     else:
#         form = ()
#         print('address not created')

#     return render(request,'customer_address.html',{'form':form})





# def login(request):
#     if 'username' in request.session:
#         return redirect('crm_app:index')
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             request.session['username'] = username
#             auth.login(request,user)
#             return redirect("crm_app:index")
#         else:
#             print('invalid details')
#             messages.info(request,"invalid details")
#             return redirect("crm_app:login")
#     else:
#         return render(request,"login.html")    



def logout(request):
    auth.logout(request)
    return redirect("crm_app:staff_login")



# STAFF ACCOUNT SECTION

def staff_register(request):
    if "username" in request.session:
        return redirect('crm_app:index')
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("username alredy exists")
                messages.info(request,"username already exist")
                return redirect("crm_app:staff_register")
            elif User.objects.filter(email=email).exists():
                print("email alredy exists")
                messages.info(request,"email  already registered")
                return redirect("crm_app:staff_register")
            else:
                user = User.objects.create_user(username=username, email=email,
                                        password=password1)
                user.save();
                print("user created")
        else:
            print("password not matched")
            return redirect('crm_app:staff_register')
        return redirect("crm_app:staff_login")
    else:
        return render(request,'staff_register.html')



def staff_login(request):
    if 'username' in request.session:
        return redirect('crm_app:index')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            request.session['username'] = username
            auth.login(request,user)
            return redirect("crm_app:index")
        else:
            print('invalid details')
            messages.info(request,"invalid details")
            return redirect("crm_app:staff_login")
    else:
        return render(request,'staff_login.html')



def invoice_pdf(request,cart_items=None,total=0,count=0):
    ct = CartList.objects.get(cart_id=c_id(request))
    ct_items = Items.objects.filter(cart=ct,active=True) 
    for i in ct_items:
        total += i.total
        count += i.quantity
    template_path = 'invoice_pdf.html'
    context = {"ct_items":ct_items, "total":total, "count":count,"user":request.user}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="inoice_details.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html,dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string



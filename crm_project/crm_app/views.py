from django.core.exceptions import ObjectDoesNotExist, RequestAborted
from django.http.response import HttpResponse, ResponseHeaders
from django.shortcuts import redirect, render,get_object_or_404
from crm_app.models import Customer, Leads, Products,CartList,Items,Quotation_Details
from .forms import CustomerAddForm, LeadAddForm, ProjectManagementAddForm,ToolsManagementUpdate,Quotation_DetailsForm
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
import datetime
from tools_management_app.models import Tools_item
# Create your views here.


def index(request):
    if 'username' in request.session:
        # STAFF SIDE
        my_open_leads  = Leads.objects.filter(lead_status="open leads",staff_name__username=request.user.username)
        total_leads =  Leads.objects.filter(staff_name__username=request.user.username).count()
        today_date = datetime.date.today()
        # day_count = today_date-datetime.timedelta(days=1*1)
        today_leads = Leads.objects.filter(date=today_date,staff_name__username=request.user.username).count()
        closed_leads = Leads.objects.filter(lead_status="close leads",staff_name__username=request.user.username).count()
        pending_leads = Leads.objects.filter(lead_status = "pending leads",staff_name__username=request.user.username).count()
        # ADMIN SIDE
        total_leadss = Leads.objects.all().count()
        today_leadss = Leads.objects.filter(date=today_date).count()
        total_closed_leadss = Leads.objects.filter(lead_status="close leads").count()
        today_closed_leadss = Leads.objects.filter(date=today_date,lead_status="close leads").count()
        total_pending_leadss = Leads.objects.filter(lead_status = "pending leads").count()
        today_pending_leadss = Leads.objects.filter(lead_status = "pending leads",date=today_date).count()
        recent_open_leads = Leads.objects.filter(lead_status = "open leads").order_by('-id')[:5]

        context = {
            'my_open_leads':my_open_leads,
            'total_leads':total_leads,
            'today_leads':today_leads,
            'total_leadss':total_leadss,
            'today_leadss': today_leadss,
            'total_closed_leadss': total_closed_leadss,
            'total_pending_leadss':total_pending_leadss,
            'closed_leads':closed_leads,
            'pending_leads':pending_leads,
            'today_closed_leadss':today_closed_leadss,
            'today_pending_leadss':today_pending_leadss,
            'recent_open_leads':recent_open_leads
        }
        return render(request,'index.html',context)
    else:
        return redirect('crm_app:staff_login')


def chat(request):
    return render(request,'chat.html')




def register(request):
    return render(request,"register.html")


def starter(request):
    return render(request,'pages-starter.html')


def customer(request):
    # STAFF VIEW
    customer = Customer.objects.filter(staff_name__username=request.user.username)
    # ADMIN VIEW
    customerr = Customer.objects.all()
    return render(request,"customer.html",{'customer':customer,'customerr':customerr})


def add_customer(request):
    form = CustomerAddForm()
    if request.method == 'POST':
        form = CustomerAddForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            staff_name = User.objects.get(username=request.user.username)
            data.staff_name = staff_name
            data.save()
            return redirect('crm_app:customers')
    else:
        form = CustomerAddForm()
    return render(request,'addcustomer.html',{'form':form})


def leads(request):
    # STAFF SIDE
    leads = Leads.objects.filter(staff_name__username=request.user.username).order_by('-id')
    # ADMIN SIDE
    all_leads = Leads.objects.all().order_by('-id')
    return render(request,"leads.html",{'leads':leads,'all_leads':all_leads})

def add_leads(request):
    fm = LeadAddForm()
    if request.method == 'POST':
        fm = LeadAddForm(request.POST,request.FILES)
        if fm.is_valid():
            data = fm.save(commit=False)
            staff_name = User.objects.get(username=request.user.username)
            data.staff_name = staff_name
            data.save()
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




def pending_leads(request):
    # STAFF SIDE
    pending_leads = Leads.objects.filter(lead_status='pending leads',staff_name__username=request.user.username)
    # ADMIN SIDE
    pending_leadss = Leads.objects.filter(lead_status='pending leads')
    return render(request,'pending_leads.html',{'pending_leads':pending_leads,'pending_leadss':pending_leadss})


def open_leads(request):
    # STAFF SIDE
    open_leads = Leads.objects.filter(lead_status="open leads",staff_name__username=request.user.username)
    # ADMIN SIDE
    open_leadss = Leads.objects.filter(lead_status='open leads')
    return render(request,'open_leads.html',{'open_leads':open_leads,'open_leadss':open_leadss})

def closed_leads(request):
    # STAFF SIDE
    closed_leads = Leads.objects.filter(lead_status="close leads",staff_name__username=request.user.username)
    # ADMIN SIDE
    closed_leadss = Leads.objects.filter(lead_status="close leads")
    return render(request,'closed_leads.html',{'close_leads':closed_leads,'closed_leadss':closed_leadss})


def customer_profile(request,customer_id):
    customer_profile= Customer.objects.filter(id=customer_id)
    return render(request,'user_profile.html',{'customer_profile':customer_profile})


def lead_search(request):
    lead = None
    Query = None
    if 'q' in request.GET:
        Query = request.GET.get('q')
        lead = Leads.objects.all().filter(Q(company_name__icontains=Query),staff_name__username=request.user.username)
    return render(request,'lead-search-result.html',{"lead":lead,"query":Query})


def pending_lead_search(request):
    junk_lead = None
    Query = None
    if 'q' in request.GET:
        Query = request.GET.get('q')
        junk_lead = Leads.objects.all().filter(Q(company_name__icontains=Query),staff_name__username=request.user.username,lead_status='pending leads')
    return render(request,'pending-lead-serch.html',{"junk_lead":junk_lead,"query":Query})


def open_lead_search(request):
    open_lead = None
    Query = None
    if 'q' in request.GET:
        Query = request.GET.get('q')
        open_lead = Leads.objects.all().filter(Q(company_name__icontains=Query),staff_name__username=request.user.username,lead_status='open leads')
    return render(request,'open-lead-serch.html',{"open_lead":open_lead,"query":Query})


def closed_lead_search(request):
    closed_lead = None
    Query = None
    if 'q' in request.GET:
        Query = request.GET.get('q')
        closed_lead = Leads.objects.all().filter(Q(company_name__icontains=Query),staff_name__username=request.user.username,lead_status='close leads')
    return render(request,'closed-lead-serch.html',{"closed_lead":closed_lead,"query":Query})





# @login_required
def Quotation_invoice(request,cart_items=None,total=0,count=0):
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
    return render(request,'Wolmart eCommmerce Marketplace HTML Template.html',{'products':products})

def Quotation_invoice_buy(request,customer_id,cart_items=None,total=0,count=0):
    customer = Customer.objects.filter(id=customer_id)
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
        ct_items = Items.objects.filter(cart=ct,active=True) 
        for i in ct_items:
            total += i.total
            count += i.quantity
    except ObjectDoesNotExist:
        return redirect("crm_app:cart2")
    return render(request,"quotation_invoice.html",{"ct_items":ct_items, "total":total, "count":count,'customer':customer})


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
        # staff_name = User.objects.get(username=request.user.username)
        c_items = Items.objects.get(prodt=product,cart=ct)
        # c_items.user = staff_name
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
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.get(username=request.POST.get('username'))
                print('username already taken')
                return render(request,'staff_register.html',{'error':"Username alredy taken"})
                
            except User.DoesNotExist:
                
                user = User.objects.create_user(username = request.POST.get('username'), password = request.POST.get('password1'),email=request.POST.get('email'))
                emp_name = request.POST.get('emp_name')
                address = request.POST.get('address')
                dob = request.POST.get('dob')
                bloodgroup = request.POST.get('bloodgroup')
                phn = request.POST.get('phn')
                staff = request.POST.get('staff')
                superviser = request.POST.get('supervisor')
                extenduser = ExtendedUserModel(dob=dob,phn_number=phn,employe_name=emp_name,user=user,address=address,blood_group=bloodgroup,is_staff2=staff,is_superviser=superviser)
                extenduser.save();
                print('user created')
                auth.login(request,user)
                return redirect('crm_app:staff_login')
        else:
            print('password not matching')
            return render(request,'staff_register.html',{'error':'password doesnot match'})
    else:
        return render(request,'staff_register.html')



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


def admin_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")  
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("username alredy exists")
                messages.info(request,"username already exist")
                return redirect("crm_app:admin_register")
            elif User.objects.filter(email=email).exists():
                print("email alredy exists")
                messages.info(request,"email  already registered")
                return redirect("crm_app:admin_register")
            else:
                user = User.objects.create_user(username=username,email=email,password=password1,is_superuser=True,is_active=True,is_staff=True)
                user.save();
                print('user created')
                return redirect('crm_app:staff_login')
        else:
            print('Password Not Matched')
            return redirect('crm_app:admin_register')    
    return render(request,"admin-register.html")


# def sitestaff_register(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password1 = request.POST.get("password1")
#         password2 = request.POST.get("password2")  
#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 print("username alredy exists")
#                 messages.info(request,"username already exist")
#                 return redirect("crm_app:sitestaff_register")
#             elif User.objects.filter(email=email).exists():
#                 print("email alredy exists")
#                 messages.info(request,"email  already registered")
#                 return redirect("crm_app:sitestaff_register")
#             else:
#                 user = User.objects.create_user(username=username,email=email,password=password1,is_active=True,is_staff=True)
#                 user.save();
#                 print('user created')
#                 return redirect('crm_app:staff_login')
#         else:
#             print('Password Not Matched')
#             return redirect('crm_app:sitestaff_register')    
#     return render(request,"sitestaff-register.html")



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
    if 'username' in request.session:
        request.session.flush();
    return redirect("crm_app:staff_login")



# STAFF ACCOUNT SECTION

# def staff_register(request):
#     if "username" in request.session:
#         return redirect('crm_app:index')
#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password1 = request.POST.get("password1")
#         password2 = request.POST.get("password2")
#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 print("username alredy exists")
#                 messages.info(request,"Username already exist")
#                 return redirect("crm_app:staff_register")
#             elif User.objects.filter(email=email).exists():
#                 print("email alredy exists")
#                 messages.info(request,"Email  already registered")
#                 return redirect("crm_app:staff_register")
#             else:
#                 user = User.objects.create_user(username=username, email=email,
#                                         password=password1)
#                 user.save();
#                 print("user created")
#         else:
#             print("password not matched")
#             return redirect('crm_app:staff_register')
#         return redirect("crm_app:staff_login")
#     else:
#         return render(request,'staff_register.html')



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
            print('logged in')
            return JsonResponse(
                {'success':True},
                safe=False
            )
        else:
            auth.login
            return JsonResponse(
                {'success':False},
                safe=False
            )
    else:
        return render(request,'staff_login.html')



def invoice_pdf(request,customer_id,cart_items=None,total=0,count=0):
    customer = Customer.objects.filter(id=customer_id)
    ct = CartList.objects.get(cart_id=c_id(request))
    ct_items = Items.objects.filter(cart=ct,active=True) 
    for i in ct_items:
        total += i.total
        count += i.quantity
    template_path = 'invoice_pdf.html'
    context = {"ct_items":ct_items, "total":total, "count":count,"user":request.user,'customer':customer}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="inoice_details.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html,dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def project_management(request):
    # staff side
    closed_leads = Leads.objects.filter(lead_status='close leads',staff_name__username=request.user.username)
    # admin side
    closed_leadss = Leads.objects.filter(lead_status='close leads').order_by('-id')
    return render(request,'project-management.html',{'closed_leads':closed_leads,'closed_leadss':closed_leadss})

def ProjectManagementUpdate(request,item_id):
    if request.method == 'POST':
        update  = Leads.objects.get(id=item_id)
        fm = ProjectManagementAddForm(request.POST,instance=update)
        if fm.is_valid():
            fm.save()
            return redirect("crm_app:project_management")
    else:
        update  = Leads.objects.get(id=item_id)
        fm = ProjectManagementAddForm(instance=update)
    return render(request,"prjct-managemnt-update.html",{'form':fm})

def tools_management(request):
    # staff side
    closed_leads = Leads.objects.filter(lead_status='close leads',staff_name__username=request.user.username)    
    # admin side
    closed_leadss = Leads.objects.filter(lead_status='close leads').order_by('-id')

        
    return render(request,'tools-management.html',{'closed_leads':closed_leads,'closed_leadss':closed_leadss})


def tools_management_update(request,item_id):
    tools = Tools_item.objects.all()
    if request.method == 'POST':
        update  = Leads.objects.get(id=item_id)
        fm = ToolsManagementUpdate(request.POST,instance=update)
        if fm.is_valid():
            data = fm.save(commit=False)
            site_staff_name = User.objects.get(username=request.user.username)
            data.site_staff_name = site_staff_name
            data.save()
            return redirect('crm_app:tools_management')
    else:
        update  = Leads.objects.get(id=item_id)
        fm = ToolsManagementUpdate(instance=update)
    return render(request,'tools-management-update.html',{'form':fm,'tools':tools})



def product_new(request):
    products = Products.objects.all()
    return render(request,'product-new.html',{'products':products})



# PRODUCT SECTION

def cctv(request):
    cctv_obj = Products.objects.filter(category__name ='Cctv')
    return render(request,'cctv.html',{'products':cctv_obj})

def video_door_phone(request):
    video_door_phone = Products.objects.filter(category__name ='Video Door Phone')
    return render(request,'video-door-phone.html',{'products':video_door_phone})

def projector(request):
    projector = Products.objects.filter(category__name ='Projector')
    return render(request,'projector.html',{'products':projector})
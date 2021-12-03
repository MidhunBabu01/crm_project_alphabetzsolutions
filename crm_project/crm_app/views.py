from django.shortcuts import redirect, render
from .models import Customer
from .forms import CustomerAddForm


# Create your views here.
def index(request):
    return render(request,'index.html')



def calendar(request):
    return render(request,"calendar.html")


def chat(request):
    return render(request,'chat.html')


def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('userpassword')
        if username == 'Midhun' and password=='123':
            return redirect('crm_app:index')
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


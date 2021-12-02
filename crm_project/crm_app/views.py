from django.shortcuts import redirect, render

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


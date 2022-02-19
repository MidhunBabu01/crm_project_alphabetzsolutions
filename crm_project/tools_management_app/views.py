from django.shortcuts import get_object_or_404, redirect, render
from tools_management_app.models import CartListt, Itemss, Tools_item
from django.core.exceptions import ObjectDoesNotExist
# from tools_management_app.models import *

# Create your views here.
def cart(request,total=0,count=0,cart_items=None):
    try:
        ct = CartListt.objects.get(cart_id=c_idd(request))
        ct_items = Itemss.objects.filter(cart=ct,active=True) 
        for i in ct_items:
            total += i.total
            count += i.quantity    
    except ObjectDoesNotExist:
        return redirect("crm_app:cart2")
    return render(request,"tools-management-update.html.html",{"ct_items":ct_items, "total":total, "count":count})




def c_idd(request):
    cartt_id = request.session.session_key
    if not cartt_id:
        cartt_id = request.session.create()
    return cartt_id


def add_cart(request,id):
    productt = Tools_item.objects.get(id=id)
    try:
        ct = CartListt.objects.get(cart_id=c_idd(request))
    except CartListt.DoesNotExist:
        ct = CartListt.objects.create(cart_id=c_idd(request))
        ct.save()
    try:
        c_items = Itemss.objects.get(prodt=productt,cart=ct)
        if c_items.quantity < c_items.prodt.stock:
            c_items.quantity+=1
        c_items.save()
    except Itemss.DoesNotExist:  
        c_items =Itemss.objects.create(prodt=productt,quantity=1,cart=ct)
        c_items.save()
    return redirect("tools_management_app:project_management_update")


def buy_now(request,product_id):
    tools = Tools_item.objects.get(id=product_id)
    try:
        ct = CartListt.objects.get(cart_id=c_idd(request))
    except CartListt.DoesNotExist:
        ct = CartListt.objects.create(cart_id=c_idd(request))
        ct.save()
    try:
        c_items = Itemss.objects.get(prodt=tools,cart=ct)
        if c_items.quantity < c_items.prodt.stock:
            c_items.quantity+=1
        c_items.save()
    except Itemss.DoesNotExist:
        c_items =Itemss.objects.create(prodt=tools,quantity=1,cart=ct)
        c_items.save()
    return redirect("tools_management_app:project_management_update")


def minus_button(request, product_id):
    ct = CartListt.objects.get(cart_id=c_idd(request))
    prod = get_object_or_404(Tools_item,id=product_id)
    c_items = Itemss.objects.get(prodt=prod, cart=ct)
    if c_items.quantity>1:
        c_items.quantity-=1
        c_items.save()
    else:  
        c_items.delete()
    return redirect("tools_management_app:addd_cart")

def delete_button(request,product_id):
    ct = CartListt.objects.get(cart_id=c_idd(request))
    prod = get_object_or_404(Tools_item,id=product_id)
    c_items = Itemss.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect("crm_app:addcart")

def count(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct = CartListt.objects.filter(cart_id=c_idd(request))
            cti = Itemss.objects.all().filter(cart=ct)
            for c in cti:
                item_count+=c.quantity
        except CartListt.DoesNotExist:
            item_count = 0
        return render({"count":item_count})     
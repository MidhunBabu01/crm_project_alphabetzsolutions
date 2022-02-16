from django.shortcuts import get_object_or_404, redirect, render
from tools_management_app.models import CartList, Items
from django.core.exceptions import ObjectDoesNotExist
from tools_management_app.models import *

# Create your views here.
def cart(request,total=0,count=0,cart_items=None):
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
        ct_items = Items.objects.filter(cart=ct,active=True) 
        for i in ct_items:
            total += i.total
            count += i.quantity    
    except ObjectDoesNotExist:
        return redirect("crm_app:cart2")
    return render(request,"ca rt.html",{"ct_items":ct_items, "total":total, "count":count})




def c_id(request):
    carttt_id = request.session.session_key
    if not carttt_id:
        carttt_id = request.session.create()
    return carttt_id


def add_cart(request,product_id):
    product = Tools_item.objects.get(id=product_id)
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
    return redirect("tools_management_app:project_management_update")
# tools_management_update


def buy_now(request,product_id):
    product = Tools_item.objects.get(id=product_id)
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
    prod = get_object_or_404(Tools_item,id=product_id)
    c_items = Items.objects.get(prodt=prod, cart=ct)
    if c_items.quantity>1:
        c_items.quantity-=1
        c_items.save()
    else:  
        c_items.delete()
    return redirect("tools_management_app:addcart")

def delete_button(request,product_id):
    ct = CartList.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Tools_item,id=product_id)
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
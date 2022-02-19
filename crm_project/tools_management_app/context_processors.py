
from . models import *
from . views import *


def countt(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct = CartListt.objects.filter(cart_id=c_idd(request))
            cti = Itemss.objects.all().filter(cart=ct[:1])
            for c in cti:
                item_count+=c.quantity
        except CartListt.DoesNotExist:
            item_count = 0
        return dict(itcc=item_count)        
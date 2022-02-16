from django.urls import path,include
from tools_management_app import views


app_name = 'tools_management_app'



urlpatterns = [
    # path('',views.staff_login,name="staff_login"),
    path('cart/', views.cart, name='addcart'),
    path('add-cart/<int:product_id>/',views.add_cart,name="add_cart"),
    path('cartDetails/<int:product_id>/',views.buy_now,name="cartDetails"),
    path('min_product/<int:product_id>/',views.minus_button,name="minus"),
    path('del-product/<int:product_id>/',views.delete_button,name="del_product"),


]
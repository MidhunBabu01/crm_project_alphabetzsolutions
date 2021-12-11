from django.urls import path,include
from crm_app import views

app_name = 'crm_app'



urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('starter/', views.starter, name='starter'),
    path('customers/', views.customer, name='customers'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('leads/', views.leads, name='leads'),
    path('add-leads/', views.add_leads, name='add_leads'),
    path('junk-leads/', views.junk_leads, name='junk_leads'), 
    path('open-leads/', views.open_leads, name='open_leads'),
    path('closed-leads/', views.closed_leads, name='closed_leads'),
    path('customer-profile/<int:customer_id>', views.customer_profile, name='customer_profile'),
    path('quotation-invoice/', views.Quotation_invoice, name='quotation_invoice'),
    path('products/', views.products, name='products'),
    path('search-result/', views.search, name='search'),
    path('cart/', views.cart, name='addcart'),
    path('cart-empty/', views.cart2, name='cart2'),
    path('cartDetails/<int:product_id>/',views.add_cart,name="cartDetails"),
    path('min_product/<int:product_id>/',views.minus_button,name="minus"),
    path('del-product/<int:product_id>/',views.delete_button,name="del_product"),

]
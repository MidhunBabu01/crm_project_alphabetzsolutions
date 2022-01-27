from django.urls import path,include
from crm_app import views


app_name = 'crm_app'



urlpatterns = [
    # customer account section
    # path('login/', views.login, name='login'),
    path('',views.staff_login,name="staff_login"),
    path('index/', views.index, name='index'),
    path('logout/',views.logout,name="logout"),
    path('register/', views.register, name='register'),
    path('**admin-register**/', views.admin_register, name='admin_register'),
    # staff account section
    path('**staff-register**/',views.staff_register,name="staff_register"),
    # path('staff-login/',views.staff_login,name="staff_login"),
    path('register/', views.register, name='register'),
    path('starter/', views.starter, name='starter'),
    path('customers/', views.customer, name='customers'),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('leads/', views.leads, name='leads'),
    path('add-leads/', views.add_leads, name='add_leads'),
    path('leads-update/<int:item_id>', views.lead_update, name='leads_edit'),
    path('leads-delete/<int:item_id>', views.lead_delete, name='leads_delete'),
    path('junk-leads/', views.pending_leads, name='junk_leads'),
    path('junk-leads-search-result/', views.pending_lead_search, name='junk_lead_search'),
    path('open-leads/', views.open_leads, name='open_leads'),
    path('closed-leads/', views.closed_leads, name='closed_leads'),
    path('lead-search/', views.lead_search, name='lead_search'),
    path('customer-profile/<int:customer_id>', views.customer_profile, name='customer_profile'),
    path('quotation-invoice/', views.Quotation_invoice, name='quotation_invoice'),
    path('products/', views.products, name='products'),
    path('search-result/', views.search, name='search'),
    path('cart/', views.cart, name='addcart'),
    path('cart-empty/', views.cart2, name='cart2'),
    path('add-cart/<int:product_id>/',views.add_cart,name="add_cart"),
    path('cartDetails/<int:product_id>/',views.buy_now,name="cartDetails"),
    path('min_product/<int:product_id>/',views.minus_button,name="minus"),
    path('del-product/<int:product_id>/',views.delete_button,name="del_product"),
    path('invoice-pdf/<int:customer_id>',views.invoice_pdf,name="invoice_pdf"),
    path('open-lead-search-result',views.open_lead_search,name="open_lead_search"),
    path('closed-lead-search-result',views.closed_lead_search,name="closed_lead_search"),
    path('quotation-invoice-buy/<int:customer_id>/',views.Quotation_invoice_buy,name="Quotation_invoice_buy"),
    
    
    
 
    
    
    

]
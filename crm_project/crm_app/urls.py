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

]
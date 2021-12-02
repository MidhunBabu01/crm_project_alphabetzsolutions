from django.urls import path,include
from crm_app import views

app_name = 'crm_app'



urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('calendar/', views.calendar, name='calendar'),
    path('chat/', views.chat, name='chat'),
    path('register/', views.register, name='register'),
    path('starter/', views.starter, name='starter'),




]
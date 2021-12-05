from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='Supplydept_login'),
    path('mainpage/', views.mainpage, name='Supplydept_mainpage'),
    path('delivery/', views.delivery, name='Supplydept_delivery'),
    path('withdraw/', views.withdraw, name='Supplydept_withdraw'),
    path('status/', views.status, name='Supplydept_status'),
    path('about/', views.about, name='Supplydept_about'),
    path('contact/', views.contact, name='Supplydept_contact'),
    path('tempwithdraw/', views.tempwithdraw, name='Supplydept_tempwithdraw'),



]

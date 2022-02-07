from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminlogin, name='Supplydept_login'),
    path('login', views.adminlogin, name='Supplydept_login'),
    path('logout', views.logoutUser, name='Supplydept_logout'),
    path('mainpage/', views.mainpage, name='Supplydept_mainpage'),
    path('delivery/', views.delivery, name='Supplydept_delivery'),
    path('withdraw/', views.withdraw, name='Supplydept_withdraw'),
    path('status/', views.status, name='Supplydept_status'),
    path('statuslimit/', views.statuslimit, name='Supplydept_statuslimit'),
    path('about/', views.about, name='Supplydept_about'),
    path('contact/', views.contact, name='Supplydept_contact'),
    path('addaccnt/', views.addaccnt, name='Supplydept_addaccnt'),

]

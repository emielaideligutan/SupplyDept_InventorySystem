from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='Supplydept_login'),
    path('delivery', views.delivery, name='Supplydept_delivery'),
]

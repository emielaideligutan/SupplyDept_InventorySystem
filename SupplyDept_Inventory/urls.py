from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='Supplydept_login'),
]
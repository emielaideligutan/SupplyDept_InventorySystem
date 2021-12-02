#from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from SupplyDept_Inventory.models import deliveryrecords
#from . import forms

def login(request):
    return render(request, 'activities/login.html')

def mainpage(request):
    return render(request, 'activities/mainpage.html')
    
def delivery(request):
    if request.method == "POST":
        if request.POST.get('delivery_item_name') and request.POST.get('delivery_unit') and request.POST.get('delivery_quantity'):
           save_delivery_record = deliveryrecords()
           save_delivery_record.delivery_item_name = request.POST.get('delivery_item_name')
           save_delivery_record.delivery_unit = request.POST.get('delivery_unit')
           save_delivery_record.delivery_quantity = request.POST.get('delivery_quantity')
           save_delivery_record.save()

           return render (request, 'activities/delivery.html')

    else:
        return render (request, 'activities/delivery.html')

def withdraw(request):
    return render(request, 'activities/withdraw.html')

def status(request):
    return render(request, 'activities/status.html')

#from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from SupplyDept_Inventory.models import deliveryrecords
#from . import forms

from SupplyDept_Inventory.models import deliveryrecords, mainstorage

def login(request):
    return render(request, 'activities/login.html')

def mainpage(request):
    return render(request, 'activities/mainpage.html')

def about(request):
    return render(request, 'activities/about.html')

def contact(request):
    return render(request, 'activities/contact.html')
    
def delivery(request):
    information = deliveryrecords.objects.all()
    if 'delivery_item_name' in request.POST:
        text = request.POST['delivery_item_name']
        if text == '':
            information = []
        else:
            print('none')

    if request.method == "POST":
        if request.POST.get('delivery_item_name') and request.POST.get('delivery_unit') and request.POST.get('delivery_quantity'):
            save_delivery_record = deliveryrecords()
            save_delivery_record.delivery_item_name = request.POST.get('delivery_item_name')
            save_delivery_record.delivery_unit = request.POST.get('delivery_unit')
            save_delivery_record.delivery_quantity = request.POST.get('delivery_quantity')
            save_delivery_record.save()
            save_main_storage = mainstorage()
            save_main_storage.ItemName = request.POST.get('delivery_item_name')
            save_main_storage.Quantity = request.POST.get('delivery_quantity')
            save_main_storage.Unit = request.POST.get('delivery_unit')
            save_main_storage.save()
        else:
            return render (request, 'activities/delivery.html')

    context = {
        'information' : information,
        }
    return render (request, 'activities/delivery.html', context)
    

def withdraw(request):
    result = mainstorage.objects.all()
    if 'delivery_item_name' in request.POST:
        text = request.POST['delivery_item_name']
        if text == '':
            result = []
        else:
            print('none')

    context = {
        'information' : result,
        }
    return render (request, 'activities/withdraw.html', context)
    

def tempwithdraw(request):
    return render(request, 'activities/tempwithdraw.html')

def status(request):
    return render(request, 'activities/status.html')

def statusupdate(request):
    return render(request, 'activities/statusupdate.html')



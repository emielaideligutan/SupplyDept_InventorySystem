#from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from SupplyDept_Inventory.models import deliveryrecords
#from . import forms

from SupplyDept_Inventory.models import deliveryrecords, mainstorage, withdrawrecords

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

            if mainstorage.objects.filter(ItemName = request.POST.get('delivery_item_name')).exists() == True:
                
                information1 = mainstorage.objects.get(ItemName = request.POST.get('delivery_item_name'))
                updating = int(information1.Quantity) + int(request.POST.get('delivery_quantity'))
                update_mainstorage = mainstorage()
                update_delivery_record = deliveryrecords()
                update_mainstorage.ItemName = request.POST.get('delivery_item_name')
                update_mainstorage.Unit = request.POST.get('delivery_unit')
                update_mainstorage.Quantity = updating
                mainstorage.objects.filter(ItemName = request.POST.get('delivery_item_name')).delete()
                update_mainstorage.save()
                information2 = mainstorage.objects.get(ItemName = request.POST.get('delivery_item_name'))
                update_delivery_record.delivery_item_name = request.POST.get('delivery_item_name')
                update_delivery_record.delivery_description = request.POST.get('delivery_description')
                update_delivery_record.delivery_unit = request.POST.get('delivery_unit')
                update_delivery_record.delivery_quantity = request.POST.get('delivery_quantity')
                update_delivery_record.delivery_remaining = information2.Quantity
                update_delivery_record.save()

   
            elif mainstorage.objects.filter(ItemName = request.POST.get('delivery_item_name')).exists() == False:
                save_delivery_record = deliveryrecords()
                save_delivery_record.delivery_item_name = request.POST.get('delivery_item_name')
                save_delivery_record.delivery_unit = request.POST.get('delivery_unit')
                save_delivery_record.delivery_description = request.POST.get('delivery_description')
                save_delivery_record.delivery_quantity = request.POST.get('delivery_quantity')
                save_delivery_record.delivery_remaining = 0
                save_delivery_record.save()
                save_main_storage = mainstorage()
                save_main_storage.ItemName = request.POST.get('delivery_item_name')
                save_main_storage.Quantity = request.POST.get('delivery_quantity')
                save_main_storage.Unit = request.POST.get('delivery_unit')
                save_main_storage.save()
            else:
                return render (request, 'activities/delivery.html')
        else:
            return render (request, 'activities/delivery.html')

    context = {
        'information' : information,
        }
    return render (request, 'activities/delivery.html', context)

def withdraw(request):
    information = mainstorage.objects.all()
    if 'ItemName' in request.POST:
        text = request.POST['ItemName']
        if text == '':
            information = []
        else:
            print('none')
    
    context = {
        'information' : information,
        }
    return render (request, 'activities/withdraw.html', context)

def tempwithdraw(request):

    if request.method == "POST":

        if request.POST.get('withdraw_item_name') and request.POST.get('withdraw_unit') and request.POST.get('withdraw_quantity'):

            if mainstorage.objects.filter(ItemName = request.POST.get('withdraw_item_name')).exists() == True:
                
                information1 = mainstorage.objects.get(ItemName = request.POST.get('withdraw_item_name'))
                updating = int(information1.Quantity) - int(request.POST.get('withdraw_quantity'))
                update_mainstorage = mainstorage()
                update_withdraw_record = withdrawrecords()
                update_mainstorage.ItemName = request.POST.get('withdraw_item_name')
                update_mainstorage.Unit = request.POST.get('withdraw_unit')
                update_mainstorage.Quantity = updating
                mainstorage.objects.filter(ItemName = request.POST.get('withdraw_item_name')).delete()
                update_mainstorage.save()
                update_withdraw_record.withdraw_item_name = request.POST.get('delivery_item_name')
                update_withdraw_record.withdraw_unit = request.POST.get('delivery_unit')
                update_withdraw_record.withdraw_quantity = request.POST.get('delivery_quantity')
                update_withdraw_record.save()

            else: 
                return render(request, 'activities/tempwithdraw.html')
    return render(request, 'activities/tempwithdraw.html')

def status(request):
    information = mainstorage.objects.all()
    if 'ItemName' in request.POST:
        text = request.POST['ItemName']
        if text == '':
            information = []
        else:
            print('none')
    
    context = {
        'information' : information,
        }
    return render (request, 'activities/status.html', context)


def changestatus(request, pk):
    data = mainstorage.objects.get(id=pk)
    information = mainstorage(instance=data)
    form = mainstorage()
    if request.method == 'POST':
        form = mainstorage(request.POST, instance=data)
        if form.is_valid():
            return redirect('/status')

    context = {
        'information' : information,
        }
    return render (request, 'activities/status.html', context)

def statuslimit(request):
    return render(request, 'activities/statuslimit.html')


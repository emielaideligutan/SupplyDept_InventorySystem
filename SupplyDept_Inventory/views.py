#from django import forms
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, response
from SupplyDept_Inventory.models import deliveryrecords
#from . import forms
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def addaccnt(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account is succesfully added')
            return redirect('Supplydept_login')
    context = {
        'form':form
    }
    return render(request, 'activities/addaccnt.html', {'form': form})

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            #messages.success(request, 'Welcome!')
            return redirect('Supplydept_mainpage')

        elif user is not None and user.is_active:
            login(request, user)
            return redirect('Supplydept_mainpage')

        else:
            messages.error(request, 'Invalid Credentials')
    context={}
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
    
    information1 = withdrawrecords.objects.all()
    if 'withdraw_item_name' in request.POST:
        text = request.POST['withdraw_item_name']
        if text == '':
            information1 = []
        else:
            print('none')
    
    context = {
        'information' : information,
        'information1' : information1,
        }
    return render (request, 'activities/withdraw.html', context)


def tempwithdraw(request):
    information = withdrawrecords.objects.all()
    if 'withdraw_item_name' in request.POST:
        text = request.POST['withdraw_item_name']
        if text == '':
            information = []
        else:
            print('none')


    if request.method == "POST":
        information = withdrawrecords.objects.all()
    if 'withdraw_item_name' in request.POST:
        text = request.POST['withdraw_item_name']
        if text == '':
            information = []
        else:
            print('none')


    if request.method == "POST":
        if  request.POST.get('withdraw_item_name') and request.POST.get('withdraw_unit') and request.POST.get('withdraw_quantity') and request.POST.get('withdraw_department'):
            if mainstorage.objects.filter(ItemName = request.POST.get('withdraw_item_name')).exists() and limitrecords.objects.filter(limit_item_name = request.POST.get('withdraw_item_name')).exists() == True:
                information1 = mainstorage.objects.get(ItemName = request.POST.get('withdraw_item_name'))
                c1 = int(information1.Quantity)
                c2 = int(request.POST.get('withdraw_quantity'))
                c3 = c1 >= c2
                if c3 == True: 
                    updating = int(information1.Quantity) - int(request.POST.get('withdraw_quantity'))
                    update_mainstorage = mainstorage()
                    update_withdraw_record = withdrawrecords()
                    update_mainstorage.ItemName = request.POST.get('withdraw_item_name')
                    update_mainstorage.Unit = request.POST.get('withdraw_unit')
                    update_mainstorage.Quantity = updating
                    mainstorage.objects.filter(ItemName = request.POST.get('withdraw_item_name')).delete()
                    update_mainstorage.save()
                    update_withdraw_record.withdraw_item_name = request.POST.get('withdraw_item_name')
                    update_withdraw_record.withdraw_department = request.POST.get('withdraw_department')
                    update_withdraw_record.withdraw_unit = request.POST.get('withdraw_unit')
                    update_withdraw_record.withdraw_quantity = request.POST.get('withdraw_quantity')
                    update_withdraw_record.save()
                    return redirect (request.path)
                else:
                    return redirect (request.path)
                

    context = {
        'information' : information,
        }
    return render (request, 'activities/tempwithdraw.html', context)

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



def statuslimit(request):
    information = mainstorage.objects.all()
    if 'ItemName' in request.POST:
        text = request.POST['ItemName']
        if text == '':
            information = []
        else:
            print('none')


    limit = limitrecords.objects.all()
    if 'limit_item_name' in request.POST:
        text = request.POST['limit_item_name']
        if text == '':
            limit = []
        else:
            print('none')
    


    if request.method == "POST":
        if  request.POST.get('limit_item_name') and request.POST.get('limit_unit') and request.POST.get('limit_quantity') and request.POST.get('limit_department'):
            save_limit_record = limitrecords()
            save_limit_record.limit_item_name = request.POST.get('limit_item_name')
            save_limit_record.limit_unit = request.POST.get('limit_unit')
            save_limit_record.limit_quantity = request.POST.get('limit_quantity')
            save_limit_record.limit_department = request.POST.get('limit_department')
            save_limit_record.save()
            return redirect (request.path)

    context = {
        'information' : information,
        'limit' : limit,
     
        }
    return render(request, 'activities/statuslimit.html',context)

def statusupdate(request):

    return render(request, 'activities/statusupdate.html')

def accntsettings(request):

    return render(request, 'activities/accntsettings.html')
#from django import forms
from genericpath import exists
from turtle import update
from typing import ItemsView
from unittest import result
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, response
from SupplyDept_Inventory.models import deliveryrecords
#from . import forms
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from itertools import chain

@login_required(login_url='Supplydept_login')
def addaccnt(request):
    if  request.user.is_authenticated and request.user.is_superuser:
        form = UserCreationForm()
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account is succesfully added')
                return redirect('Supplydept_login')
            else:
                messages.error(request, 'Invalid')

    else:
        return HttpResponse('You are not authorized to access this page')
    
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

def logoutUser(request):
    logout(request)
    return render(request, 'activities/login.html')

@login_required(login_url='Supplydept_login')
def mainpage(request):
    return render(request, 'activities/mainpage.html')

@login_required(login_url='Supplydept_login')
def about(request):
    return render(request, 'activities/about.html')

@login_required(login_url='Supplydept_login')
def contact(request):
    return render(request, 'activities/contact.html')

@login_required(login_url='Supplydept_login')
def delivery(request):
    information = deliveryrecords.objects.all()
    if 'delivery_item_name' in request.POST:
        text = request.POST['delivery_item_name']
        if text == '':
            information = []
        else:
            print('none')

    if request.method == "POST":
        if request.POST.get('delivery_item_name') and request.POST.get('delivery_quantity'):
            if mainstorage.objects.filter(ItemName = request.POST.get('delivery_item_name')).exists() == True:
                information1 = mainstorage.objects.get(ItemName = request.POST.get('delivery_item_name'))
                updating = int(information1.Quantity) + int(request.POST.get('delivery_quantity'))
                update_mainstorage = mainstorage()
                update_delivery_record = deliveryrecords()
                update_mainstorage.ItemName = request.POST.get('delivery_item_name')
                update_mainstorage.Quantity = updating
                mainstorage.objects.filter(ItemName = request.POST.get('delivery_item_name')).delete()
                update_mainstorage.save()
                information2 = mainstorage.objects.get(ItemName = request.POST.get('delivery_item_name'))
                update_delivery_record.delivery_item_name = request.POST.get('delivery_item_name')
                update_delivery_record.delivery_description = request.POST.get('delivery_description')
                update_delivery_record.delivery_quantity = request.POST.get('delivery_quantity')
                update_delivery_record.delivery_remaining = information2.Quantity
                update_delivery_record.save()
                messages.success(request, 'Item Successfully Added')
                return redirect (request.path)


            elif mainstorage.objects.filter(ItemName = request.POST.get('delivery_item_name')).exists() == False:
                save_delivery_record = deliveryrecords()
                save_delivery_record.delivery_item_name = request.POST.get('delivery_item_name')
                save_delivery_record.delivery_description = request.POST.get('delivery_description')
                save_delivery_record.delivery_quantity = request.POST.get('delivery_quantity')
                save_delivery_record.delivery_remaining = 0
                save_delivery_record.save()
                save_main_storage = mainstorage()
                save_main_storage.ItemName = request.POST.get('delivery_item_name')
                save_main_storage.Quantity = request.POST.get('delivery_quantity')
                save_main_storage.save()
                messages.success(request, 'Item Successfully Added')
                return redirect (request.path)
            else:
                return render (request, 'activities/delivery.html')
        else:
            messages.error(request, 'Something is wrong please try again')
            return render (request, 'activities/delivery.html')

    context = {
        'information' : information,
        }
    return render (request, 'activities/delivery.html', context)


@login_required(login_url='Supplydept_login')
def withdraw(request):
    if  request.user.is_authenticated and request.user.is_superuser:
        information = withdrawrecords.objects.all()
        if 'withdraw_item_name' in request.GET:
            text = request.GET['withdraw_item_name']
            if text == '':
                information = []
            else:
                print('none')

        limit = limitrecords.objects.all()
        if 'limit_item_name' in request.GET:
            text = request.GET['limit_item_name']
            if text == '':
                limit = []
            else:
                print('none')


        if 'search_department' in request.GET:
            search_department = request.GET['search_department']
            limit = limitrecords.objects.filter(limit_department=search_department)
        else:
            limit = limitrecords.objects.all()


        if request.method == "GET":
            if  request.GET.get('withdraw_quantity'):
                if limitrecords.objects.filter(limit_id = request.GET.get('withdraw_id')).exists() == True:
                    if mainstorage.objects.filter(ItemName = limitrecords.objects.get(limit_id = request.GET.get('withdraw_id')).limit_item_name).exists == True:
                        updatelimit = limitrecords()
                        information1 = mainstorage.objects.get(ItemName = limitrecords.objects.get(limit_id = request.GET.get('withdraw_id')).limit_item_name)
                        updatelimit.limit_id = request.GET.get('withdraw_id')
                        updatelimit.limit_item_name = limitrecords.objects.get(limit_id = request.GET.get('withdraw_id')).limit_item_name
                        updatelimit.limit_quantity = int(limitrecords.objects.get(limit_id = request.GET.get('withdraw_id')).limit_quantity) - int(request.GET.get('withdraw_quantity'))
                        updatelimit.limit_department = limitrecords.objects.get(limit_id = request.GET.get('withdraw_id')).limit_department
                        updatewithdraw = withdrawrecords()
                        updatewithdraw.withdraw_item_name = limitrecords.objects.get(limit_id = request.GET.get('withdraw_id')).limit_item_name
                        updatewithdraw.withdraw_quantity = request.GET.get('withdraw_quantity')
                        updatewithdraw.withdraw_department = limitrecords.objects.get(limit_id = request.GET.get('withdraw_id')).limit_department
                        update_mainstorage = mainstorage()
                        update_mainstorage.ItemName = limitrecords.objects.get(limit_id = request.GET.get('withdraw_id')).limit_item_name
                        update_mainstorage.Quantity = int(information1.Quantity) - int(request.GET.get('withdraw_quantity'))
                        if updatelimit.limit_quantity >= 0 or update_mainstorage >= 0:
                            updatelimit.save()
                            updatewithdraw.save()
                            mainstorage.objects.filter(ItemName = limitrecords.objects.get(limit_id = request.GET.get('withdraw_id')).limit_item_name).delete()
                            update_mainstorage.save()
                        else:
                            messages.error(request, 'not enough item')
                            return redirect (request.path)
                    else:
                        messages.error(request, 'Not in the Mainstorage')
                        return redirect (request.path)
                else:
                    messages.error(request, 'Invalid Id')
                    return redirect (request.path)


        context = {
            'information' : information,
            'limit' : limit
            }
        return render (request, 'activities/withdraw.html', context)
    else:
        return HttpResponse('You are not authorized to access this page')

@login_required(login_url='Supplydept_login')
def status(request):
    if  request.user.is_authenticated and request.user.is_superuser:
        information = mainstorage.objects.all()
        if 'ItemName' in request.POST:
            text = request.POST['ItemName']
            if text == '':
                information = []
            else:
                print('none')

            return render(request, 'activities/status.html')

        if request.method == "POST":
            sitem = request.POST.get('search_item_name')
            information = mainstorage.objects.raw('select * from mainstorage where ItemName="'+sitem+'"')
        context = {
                    'information' : information
                    }
        return render(request, 'activities/status.html',context)


    else:
        return HttpResponse('You are not authorized to access this page')


@login_required(login_url='Supplydept_login')
def statuslimit(request):
    information = mainstorage.objects.all()
    if 'ItemName' in request.POST:
        text = request.POST['ItemName']
        if text == '':
            information = []
        else:
            print('none')

    sample = limitrecords.objects.all()
    if 'limit_item_name' in request.POST:
        text = request.POST['limit_item_name']
        if text == '':
            sample = []
        else:
            print('none')

    if 'search_department' in request.POST:
        search_department = request.POST['search_department']
        sample = limitrecords.objects.filter(limit_department=search_department)
    else:
        sample = limitrecords.objects.all()


    if request.method == "POST":
            if  request.POST.get('limit_item_name') and request.POST.get('limit_quantity') and request.POST.get('limit_department') and request.POST.get('limit_id'):
                if request.POST.get('limit_id') == "Not Existing":
                        save_record = limitrecords()
                        save_record.limit_item_name = request.POST.get('limit_item_name')
                        save_record.limit_quantity = request.POST.get('limit_quantity')
                        save_record.limit_department = request.POST.get('limit_department')
                        save_record.save()
                        messages.success(request, 'Limit Successfully Added')
                        return redirect (request.path)


                elif limitrecords.objects.filter(limit_id = request.POST.get('limit_id')).exists() == True:
                    if (request.POST.get('limit_item_name') == limitrecords.objects.get(limit_id = request.POST.get('limit_id')).limit_item_name) and (request.POST.get('limit_unit') == limitrecords.objects.get(limit_id = request.POST.get('limit_id')).limit_unit) and (request.POST.get('limit_department') == limitrecords.objects.get(limit_id = request.POST.get('limit_id')).limit_department):
                        information1 = limitrecords.objects.get(limit_id = request.POST.get('limit_id'))
                        updatinglimit = int(information1.limit_quantity) + int(request.POST.get('limit_quantity'))
                        update_limit_record = limitrecords()
                        update_limit_record.limit_id = request.POST.get('limit_id')
                        update_limit_record.limit_item_name = request.POST.get('limit_item_name')
                        update_limit_record.limit_department = request.POST.get('limit_department')
                        update_limit_record.limit_quantity = updatinglimit
                        limitrecords.objects.filter(limit_id = request.POST.get('limit_id')).delete()
                        update_limit_record.save()
                        messages.success(request, 'Limit Successfully Added')
                        return redirect (request.path)
                    else:
                        messages.error(request, 'Something is wrong please try again')
                        return redirect (request.path)

                else:
                        messages.error(request, 'Something is wrong please try again')
                        return redirect (request.path)




    context = {
        'information' : information,
        'sample' : sample,
        }
    return render(request, 'activities/statuslimit.html',context)

@login_required(login_url='Supplydept_login')
def statusupdate(request):
    return render(request, 'activities/statusupdate.html')
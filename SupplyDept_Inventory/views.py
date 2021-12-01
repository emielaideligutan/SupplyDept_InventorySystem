from django.shortcuts import render
from django.http import HttpResponse

from SupplyDept_Inventory.models import deliveryrecords

def login(request):
    return render(request, 'activities/login.html')

def mainpage(request):
    return render(request, 'activities/mainpage.html')

def about(request):
    return render(request, 'activities/about.html')

def contact(request):
    return render(request, 'activities/contact.html')
    
def delivery(request):
    return render(request, 'activities/delivery.html')

def withdraw(request):
    return render(request, 'activities/withdraw.html')

def tempwithdraw(request):
    return render(request, 'activities/tempwithdraw.html')

def status(request):
    return render(request, 'activities/status.html')



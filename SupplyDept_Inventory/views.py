from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return render(request, 'activities/login.html')

def mainpage(request):
    return render(request, 'activities/mainpage.html')
    
def delivery(request):
    return render(request, 'activities/delivery.html')

def withdraw(request):
    return render(request, 'activities/withdraw.html')

def status(request):
    return render(request, 'activities/status.html')

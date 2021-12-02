from django.db import models
from django.db.models import Model
from django.utils import timezone
from datetime import date
from datetime import time

# Create your models here.
class admin(models.Model):

    Admin_Username = models.CharField(max_length=50, verbose_name='admin username')
    Admin_Password = models.CharField(max_length=50, verbose_name='admin password')

def __str__(self):
    return self.Admin_Username

class withdrawrecords(models.Model):

    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    current_date = models.CharField(max_length=50, verbose_name='current date')
    current_time = models.CharField(max_length=50, verbose_name='current time')

def __str__(self):
    return self.ItemName


class deliveryrecords(models.Model):
    delivery_item_name = models.CharField(max_length=50, verbose_name='delivery_item_name')
    delivery_unit = models.CharField(max_length=50, verbose_name='delivery_unit')
    delivery_quantity = models.CharField(max_length=50, verbose_name='delivery_quantity')
    current_date = models.DateField(default=date.today, verbose_name= 'delivery_current_date')
    current_time = models.TimeField(default=timezone.now, verbose_name= 'delivery_current_date')
    #current_time = models.CharField(max_length=50, verbose_name='delivery_current_time')

    class Meta:
        db_table = ('deliveryrecords')

def __str__(self):
    return self.ItemName


class mainstorage(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')

def __str__(self):
    return self.ItemName

class OCS_CASHIER_SERVICES(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')

def __str__(self):
    return self.ItemName

class OES_EXTENSION_SERVICES(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')

def __str__(self):
    return self.ItemName

class OGS_GUIDANCE_SERVICES(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')

def __str__(self):
    return self.ItemName
    
class OHR_HUMAN_RESOURCES(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')

def __str__(self):
    return self.ItemName
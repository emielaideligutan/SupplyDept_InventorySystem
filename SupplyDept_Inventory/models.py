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

    withdraw_item_name = models.CharField(max_length=50, verbose_name='withdraw__item_name')
    withdraw_unit = models.CharField(max_length=50, verbose_name='withdraw_unit')
    withdraw_quantity = models.CharField(max_length=50, verbose_name='withdraw_quantity')
    current_date = models.DateField(default=date.today, verbose_name='withdraw_current_date')
    withdraw_department = models.CharField(max_length=50, verbose_name='withdraw_department')
    class Meta:
        db_table = "withdrawrecords"

def __str__(self):
    return self.withdraw_item_name

class deliveryrecords(models.Model):

    delivery_item_name = models.CharField(max_length=50, verbose_name='delivery_item_name')
    delivery_unit = models.CharField(max_length=50, verbose_name='delivery_unit')
    delivery_description = models.CharField(max_length=50, verbose_name='delivery_description')
    delivery_quantity = models.CharField(max_length=50, verbose_name='delivery_quantity')
    delivery_remaining = models.CharField(max_length=50, verbose_name='delivery_remaining')
    current_date = models.DateField(default=date.today, verbose_name= 'delivery_current_date')
    #current_time = models.CharField(max_length=50, verbose_name='delivery_current_time')

    class Meta:
        db_table = ('deliveryrecords')

def __str__(self):
    return self.delivery_item_name
    
class limitrecords(models.Model):

    limit_id = models.AutoField(primary_key=True)
    limit_item_name = models.CharField(max_length=50, verbose_name='limit_item_name')
    limit_quantity = models.CharField(max_length=50, verbose_name='limit_quantity')
    limit_unit = models.CharField(max_length=50, verbose_name='limit_unit')
    limit_department = models.CharField(max_length=50, verbose_name='limit_department')
    limit_code = models.CharField(max_length=50, verbose_name='limit_code')
    
    #current_time = models.CharField(max_length=50, verbose_name='delivery_current_time')

    class Meta:
        db_table = ('limitrecords')

def __str__(self):
    return self.limit_item_name

class mainstorage(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='ItemName')
    Unit = models.CharField(max_length=50, verbose_name='Unit')
    Quantity = models.CharField(max_length=50, verbose_name='Quantity')
    Remaining = models.CharField(max_length=50, verbose_name='Remaining')

    class Meta:
        db_table = "mainstorage"

def __str__(self):
    return self.ItemName


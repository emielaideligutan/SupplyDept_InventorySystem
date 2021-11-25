from django.db import models

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
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    current_date = models.CharField(max_length=50, verbose_name='current date')
    current_time = models.CharField(max_length=50, verbose_name='current time')

def __str__(self):
    return self.ItemName


class mainstorage(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')

def __str__(self):
    return self.ItemName

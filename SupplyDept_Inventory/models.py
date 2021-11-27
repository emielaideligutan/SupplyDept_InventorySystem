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
    current_date = models.DateField(max_length=50, verbose_name='current date')
    current_time = models.TimeField(max_length=50, verbose_name='current time')
    class Meta:
        db_table = "withdrawrecords"

def __str__(self):
    return self.ItemName


class deliveryrecords(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    current_date = models.DateField(max_length=50, verbose_name='current date')
    current_time = models.TimeField(max_length=50, verbose_name='current time')
    class Meta:
        db_table = "deliveryrecords"

def __str__(self):
    return self.ItemName


class mainstorage(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "mainstorage"

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

class OHS_HEALTH_SERVICES(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')

def __str__(self):
    return self.ItemName

class OIT_INFORMATION_TECHNOLOGY(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')

def __str__(self):
    return self.ItemName

class OSP_JOB_PLACEMENT(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')

def __str__(self):
    return self.ItemName

class OPR_PROCUREMENT(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')

def __str__(self):
    return self.ItemName

class ORE_RESEARCH_AND_EXTENSION(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')

def __str__(self):
    return self.ItemName
 
class ORM_RECORD_MANAGEMENT(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')

def __str__(self):
    return self.ItemName

class ORS_RESEARCH_SERVICES(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')

def __str__(self):
    return self.ItemName
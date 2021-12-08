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
    current_date = models.DateField(max_length=50, verbose_name='current date')
    current_time = models.TimeField(max_length=50, verbose_name='current time')
    class Meta:
        db_table = "withdrawrecords"

def __str__(self):
    return self.ItemName


class deliveryrecords(models.Model):

    delivery_item_name = models.CharField(max_length=50, verbose_name='delivery_item_name')
    delivery_unit = models.CharField(max_length=50, verbose_name='delivery_unit')
    delivery_description = models.CharField(max_length=50, verbose_name='delivery_description')
    delivery_quantity = models.CharField(max_length=50, verbose_name='delivery_quantity')
    delivery_remaining = models.CharField(max_length=50, verbose_name='delivery_remaining')
    current_date = models.DateField(default=date.today, verbose_name= 'delivery_current_date')
    current_time = models.TimeField(default=timezone.now, verbose_name= 'delivery_current_date')
    #current_time = models.CharField(max_length=50, verbose_name='delivery_current_time')

    class Meta:
        db_table = ('deliveryrecords')

def __str__(self):
    return self.ItemName
    
class mainstorage(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='ItemName')
    Unit = models.CharField(max_length=50, verbose_name='Unit')
    Quantity = models.CharField(max_length=50, verbose_name='Quantity')

    class Meta:
        db_table = "mainstorage"

def __str__(self):
    return self.ItemName


class OCS_CASHIER_SERVICES(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "ocs_cashier_services"

def __str__(self):
    return self.ItemName


class OES_EXTENSION_SERVICES(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "oes_extension_services"

def __str__(self):
    return self.ItemName


class OGS_GUIDANCE_SERVICES(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "ogs_guidance_services"

def __str__(self):
    return self.ItemName
    

class OHR_HUMAN_RESOURCES(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "ohr_human_resources"

def __str__(self):
    return self.ItemName


class OHS_HEALTH_SERVICES(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "ohs_health_services"

def __str__(self):
    return self.ItemName


class OIT_INFORMATION_TECHNOLOGY(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "oit_information_technology"

def __str__(self):
    return self.ItemName


class OSP_JOB_PLACEMENT(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "osp_job_placement"

def __str__(self):
    return self.ItemName


class OPR_PROCUREMENT(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "opr_procurement"

def __str__(self):
    return self.ItemName


class ORE_RESEARCH_AND_EXTENSION(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "ore_research_and_extension"

def __str__(self):
    return self.ItemName
 

class ORM_RECORD_MANAGEMENT(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "orm_record_management"

def __str__(self):
    return self.ItemName


class ORS_RESEARCH_SERVICES(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "ors_research_services"

def __str__(self):
    return self.ItemName


class OSA_STUDENT_AFFAIRS(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "osa_student_affairs"

def __str__(self):
    return self.ItemName


class OSH_SECURITY_HOUSE(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "osh_security_house"

def __str__(self):
    return self.ItemName


class DCG_DOCUMENT_CONTROL_GUIDE(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "dcg_document_control_guide"

def __str__(self):
    return self.ItemName


class DID_INDUSTRIAL_EDUCATION(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "did_industrial_education"

def __str__(self):
    return self.ItemName


class DES_ENGINEERING_TECHNOLOGY(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "des_engineering_technology"

def __str__(self):
    return self.ItemName


class DLA_LIBERAL_ARTS(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "dla_liberal_arts"

def __str__(self):
    return self.ItemName


class DLDMS_MATH_AND_SCIENCE(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "dldms_math_and_science"

def __str__(self):
    return self.ItemName


class DPECS_PHYSICALEDUCATION_CULTURAL_SPORTS(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "dpecs_physicaleducation_cultural_sports"

def __str__(self):
    return self.ItemName


class DPBETEEAP(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "dpbeteeap"

def __str__(self):
    return self.ItemName


class GAD_GENDER_AND_DEVELOPMENT(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "gad_gender_and_development"

def __str__(self):
    return self.ItemName


class IDO_INFRASTRUCTURE_DEVELOPMENT_OFFICE(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "ido_infrastructure_development_office"

def __str__(self):
    return self.ItemName


class NSTP(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "nstp"

def __str__(self):
    return self.ItemName


class OAA_ACADEMIC_AFFAIRS(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "oaa_academic_affairs"

def __str__(self):
    return self.ItemName


class OAC_ACCOUNTING_CAMPUS(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "oac_accounting_campus"

def __str__(self):
    return self.ItemName


class OAD_ADMISSION(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "oad_admission"

def __str__(self):
    return self.ItemName


class OAF_ADMIN_AND_FINANCE(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "oaf_admin_and_finance"

def __str__(self):
    return self.ItemName


class OAL_ALUMNI(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "oal_alumni"

def __str__(self):
    return self.ItemName


class OAS_ADMIN_SERVICES(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "oas_admin_services"

def __str__(self):
    return self.ItemName


class OAX_AUXILIARY(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "oax_auxiliary"

def __str__(self):
    return self.ItemName


class OBA_BIDS_AND_AWARDS(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "oba_bids_and_awards"

def __str__(self):
    return self.ItemName


class OBD_BUDGET_DEVELOPMENT(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "obd_budget_development"

def __str__(self):
    return self.ItemName


class OCD_CAMPUS_DIRECTOR(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "ocd_campus_director"

def __str__(self):
    return self.ItemName


class OCL_CAMPUS_LIBRARY(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "ocl_campus_library"

def __str__(self):
    return self.ItemName


class OCP_CAMPUS_PLANNING(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "ocp_campus_planning"

def __str__(self):
    return self.ItemName


class OCR_CAMPUS_REGISTRAR(models.Model):
    ItemName = models.CharField(max_length=50, verbose_name='item name')
    Unit = models.CharField(max_length=50, verbose_name='unit')
    Quantity = models.CharField(max_length=50, verbose_name='quantity')
    class Meta:
        db_table = "ocr_campus_register"

def __str__(self):
    return self.ItemName

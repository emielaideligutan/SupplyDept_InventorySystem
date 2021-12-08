
# Generated by Django 3.2.8 on 2021-12-02 03:17
import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Admin_Username', models.CharField(max_length=50, verbose_name='admin username')),
                ('Admin_Password', models.CharField(max_length=50, verbose_name='admin password')),
            ],
        ),
        migrations.CreateModel(
            name='DCG_DOCUMENT_CONTROL_GUIDE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'dcg_document_control_guide',
            },
        ),
        migrations.CreateModel(
            name='deliveryrecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_item_name', models.CharField(max_length=50, verbose_name='delivery_item_name')),
                ('delivery_description', models.CharField(max_length=50, verbose_name='delivery_description')),
                ('delivery_unit', models.CharField(max_length=50, verbose_name='delivery_unit')),
                ('delivery_quantity', models.CharField(max_length=50, verbose_name='delivery_quantity')),
                ('delivery_remaining', models.CharField(max_length=50, verbose_name='delivery_remaining')),
                ('current_date', models.DateField(default=datetime.date.today, verbose_name='delivery_current_date')),
                ('current_time', models.TimeField(default=django.utils.timezone.now, verbose_name='delivery_current_date')),
            ],
            options={
                'db_table': 'deliveryrecords',
            },
        ),
        migrations.CreateModel(
            name='DES_ENGINEERING_TECHNOLOGY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'des_engineering_technology',
            },
        ),
        migrations.CreateModel(
            name='DID_INDUSTRIAL_EDUCATION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'did_industrial_education',
            },
        ),
        migrations.CreateModel(
            name='DLA_LIBERAL_ARTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'dla_liberal_arts',
            },
        ),
        migrations.CreateModel(
            name='DLDMS_MATH_AND_SCIENCE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'dldms_math_and_science',
            },
        ),
        migrations.CreateModel(
            name='DPBETEEAP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'dpbeteeap',
            },
        ),
        migrations.CreateModel(
            name='DPECS_PHYSICALEDUCATION_CULTURAL_SPORTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'dpecs_physicaleducation_cultural_sports',
            },
        ),
        migrations.CreateModel(
            name='GAD_GENDER_AND_DEVELOPMENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'gad_gender_and_development',
            },
        ),
        migrations.CreateModel(
            name='IDO_INFRASTRUCTURE_DEVELOPMENT_OFFICE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'ido_infrastructure_development_office',
            },
        ),
        migrations.CreateModel(
            name='mainstorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='ItemName')),
                ('Unit', models.CharField(max_length=50, verbose_name='Unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='Quantity')),
            ],
            options={
                'db_table': 'mainstorage',
            },
        ),
        migrations.CreateModel(
            name='NSTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'nstp',
            },
        ),
        migrations.CreateModel(
            name='OAA_ACADEMIC_AFFAIRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'oaa_academic_affairs',
            },
        ),
        migrations.CreateModel(
            name='OAC_ACCOUNTING_CAMPUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'oac_accounting_campus',
            },
        ),
        migrations.CreateModel(
            name='OAD_ADMISSION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'oad_admission',
            },
        ),
        migrations.CreateModel(
            name='OAF_ADMIN_AND_FINANCE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'oaf_admin_and_finance',
            },
        ),
        migrations.CreateModel(
            name='OAL_ALUMNI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'oal_alumni',
            },
        ),
        migrations.CreateModel(
            name='OAS_ADMIN_SERVICES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'oas_admin_services',
            },
        ),
        migrations.CreateModel(
            name='OAX_AUXILIARY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'oax_auxiliary',
            },
        ),
        migrations.CreateModel(
            name='OBA_BIDS_AND_AWARDS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'oba_bids_and_awards',
            },
        ),
        migrations.CreateModel(
            name='OBD_BUDGET_DEVELOPMENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'obd_budget_development',
            },
        ),
        migrations.CreateModel(
            name='OCD_CAMPUS_DIRECTOR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'ocd_campus_director',
            },
        ),
        migrations.CreateModel(
            name='OCL_CAMPUS_LIBRARY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'ocl_campus_library',
            },
        ),
        migrations.CreateModel(
            name='OCP_CAMPUS_PLANNING',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'ocp_campus_planning',
            },
        ),
        migrations.CreateModel(
            name='OCR_CAMPUS_REGISTRAR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'ocr_campus_register',
            },
        ),
        migrations.CreateModel(
            name='OCS_CASHIER_SERVICES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'ocs_cashier_services',
            },
        ),
        migrations.CreateModel(
            name='OES_EXTENSION_SERVICES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'oes_extension_services',
            },
        ),
        migrations.CreateModel(
            name='OGS_GUIDANCE_SERVICES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'ogs_guidance_services',
            },
        ),
        migrations.CreateModel(
            name='OHR_HUMAN_RESOURCES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'ohr_human_resources',
            },
        ),
        migrations.CreateModel(
            name='OHS_HEALTH_SERVICES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'ohs_health_services',
            },
        ),
        migrations.CreateModel(
            name='OIT_INFORMATION_TECHNOLOGY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'oit_information_technology',
            },
        ),
        migrations.CreateModel(
            name='OPR_PROCUREMENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'opr_procurement',
            },
        ),
        migrations.CreateModel(
            name='ORE_RESEARCH_AND_EXTENSION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'ore_research_and_extension',
            },
        ),
        migrations.CreateModel(
            name='ORM_RECORD_MANAGEMENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'orm_record_management',
            },
        ),
        migrations.CreateModel(
            name='ORS_RESEARCH_SERVICES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'ors_research_services',
            },
        ),
        migrations.CreateModel(
            name='OSA_STUDENT_AFFAIRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'osa_student_affairs',
            },
        ),
        migrations.CreateModel(
            name='OSH_SECURITY_HOUSE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'osh_security_house',
            },
        ),
        migrations.CreateModel(
            name='OSP_JOB_PLACEMENT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
            options={
                'db_table': 'osp_job_placement',
            },
        ),
        migrations.CreateModel(
            name='withdrawrecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
                ('current_date', models.DateField(max_length=50, verbose_name='current date')),
                ('current_time', models.TimeField(max_length=50, verbose_name='current time')),
            ],
            options={
                'db_table': 'withdrawrecords',
            },
        ),
    ]

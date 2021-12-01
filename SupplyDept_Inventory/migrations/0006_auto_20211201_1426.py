# Generated by Django 3.2.9 on 2021-12-01 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SupplyDept_Inventory', '0005_auto_20211127_2251'),
    ]

    operations = [
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
        migrations.AlterModelTable(
            name='ocs_cashier_services',
            table='ocs_cashier_services',
        ),
        migrations.AlterModelTable(
            name='oes_extension_services',
            table='oes_extension_services',
        ),
        migrations.AlterModelTable(
            name='ogs_guidance_services',
            table='ogs_guidance_services',
        ),
        migrations.AlterModelTable(
            name='ohr_human_resources',
            table='ohr_human_resources',
        ),
        migrations.AlterModelTable(
            name='ohs_health_services',
            table='ohs_health_services',
        ),
        migrations.AlterModelTable(
            name='oit_information_technology',
            table='oit_information_technology',
        ),
        migrations.AlterModelTable(
            name='opr_procurement',
            table='opr_procurement',
        ),
        migrations.AlterModelTable(
            name='ore_research_and_extension',
            table='ore_research_and_extension',
        ),
        migrations.AlterModelTable(
            name='orm_record_management',
            table='orm_record_management',
        ),
        migrations.AlterModelTable(
            name='ors_research_services',
            table='ors_research_services',
        ),
        migrations.AlterModelTable(
            name='osp_job_placement',
            table='osp_job_placement',
        ),
    ]

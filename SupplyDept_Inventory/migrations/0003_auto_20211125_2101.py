# Generated by Django 3.2.9 on 2021-11-25 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SupplyDept_Inventory', '0002_auto_20211118_1719'),
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
            name='deliveryrecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
                ('current_date', models.CharField(max_length=50, verbose_name='current date')),
                ('current_time', models.CharField(max_length=50, verbose_name='current time')),
            ],
        ),
        migrations.CreateModel(
            name='mainstorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
            ],
        ),
        migrations.CreateModel(
            name='withdrawrecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=50, verbose_name='item name')),
                ('Unit', models.CharField(max_length=50, verbose_name='unit')),
                ('Quantity', models.CharField(max_length=50, verbose_name='quantity')),
                ('current_date', models.CharField(max_length=50, verbose_name='current date')),
                ('current_time', models.CharField(max_length=50, verbose_name='current time')),
            ],
        ),
        migrations.DeleteModel(
            name='deliverypage',
        ),
        migrations.DeleteModel(
            name='statuspage',
        ),
        migrations.DeleteModel(
            name='withdrawpage',
        ),
    ]
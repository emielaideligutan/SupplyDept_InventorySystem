# Generated by Django 3.2.8 on 2021-12-02 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SupplyDept_Inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainstorage',
            name='ItemName',
            field=models.CharField(max_length=50, verbose_name='ItemName'),
        ),
        migrations.AlterField(
            model_name='mainstorage',
            name='Quantity',
            field=models.CharField(max_length=50, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='mainstorage',
            name='Unit',
            field=models.CharField(max_length=50, verbose_name='Unit'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-12-09 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SupplyDept_Inventory', '0002_auto_20211209_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawrecords',
            name='withdraw_item_name',
            field=models.CharField(max_length=50, verbose_name='withdraw__item_name'),
        ),
        migrations.AlterField(
            model_name='withdrawrecords',
            name='withdraw_quantity',
            field=models.CharField(max_length=50, verbose_name='withdraw_quantity'),
        ),
        migrations.AlterField(
            model_name='withdrawrecords',
            name='withdraw_unit',
            field=models.CharField(max_length=50, verbose_name='withdraw_unit'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-12-10 10:24

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SupplyDept_Inventory', '0004_auto_20211209_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawrecords',
            name='current_date',
            field=models.DateField(default=datetime.date.today, verbose_name='withdraw_current_date'),
        ),
        migrations.AlterField(
            model_name='withdrawrecords',
            name='current_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='withdarw_current_time'),
        ),
    ]

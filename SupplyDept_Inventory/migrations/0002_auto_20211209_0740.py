# Generated by Django 3.2.8 on 2021-12-08 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SupplyDept_Inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='withdrawrecords',
            old_name='ItemName',
            new_name='withdraw_item_name',
        ),
        migrations.RenameField(
            model_name='withdrawrecords',
            old_name='Quantity',
            new_name='withdraw_quantity',
        ),
        migrations.RenameField(
            model_name='withdrawrecords',
            old_name='Unit',
            new_name='withdraw_unit',
        ),
    ]
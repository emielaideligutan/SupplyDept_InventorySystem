# Generated by Django 3.2.8 on 2022-01-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SupplyDept_Inventory', '0003_auto_20211227_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainstorage',
            name='Remaining',
            field=models.CharField(default=50, max_length=50, verbose_name='Remaining'),
            preserve_default=False,
        ),
    ]
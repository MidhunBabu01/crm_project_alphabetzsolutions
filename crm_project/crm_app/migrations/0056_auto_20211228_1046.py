# Generated by Django 3.2.9 on 2021-12-28 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0055_auto_20211228_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='order_Date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 28, 10, 46, 24, 759418)),
        ),
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 12, 28, 10, 46, 24, 759418)),
        ),
    ]
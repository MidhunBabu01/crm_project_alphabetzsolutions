# Generated by Django 3.2.9 on 2022-01-01 04:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0062_auto_20211231_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 31, 9, 42, 23, 222245)),
        ),
        migrations.AlterField(
            model_name='items',
            name='order_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 1, 9, 42, 23, 222245)),
        ),
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 1, 9, 42, 23, 222245)),
        ),
    ]

# Generated by Django 3.2.9 on 2022-02-05 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0102_auto_20220205_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 7, 15, 2, 32, 655347)),
        ),
        migrations.AlterField(
            model_name='items',
            name='order_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 15, 2, 32, 655347)),
        ),
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 5, 15, 2, 32, 652349)),
        ),
    ]

# Generated by Django 3.2.9 on 2022-01-05 08:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0065_auto_20220105_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 14, 12, 3, 510175)),
        ),
        migrations.AlterField(
            model_name='items',
            name='order_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 5, 14, 12, 3, 510175)),
        ),
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 5, 14, 12, 3, 510175)),
        ),
        migrations.AlterField(
            model_name='quotation_details',
            name='quotation_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_app.customer'),
        ),
    ]

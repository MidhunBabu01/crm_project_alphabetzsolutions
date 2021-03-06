# Generated by Django 3.2.9 on 2022-03-11 05:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm_app', '0135_auto_20220310_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 10, 29, 59, 868494)),
        ),
        migrations.AlterField(
            model_name='items',
            name='order_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 11, 10, 29, 59, 868494)),
        ),
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 11, 10, 29, 59, 865496)),
        ),
        migrations.AlterField(
            model_name='task',
            name='staff_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.2.9 on 2022-03-18 05:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0141_auto_20220317_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crm_app.customer'),
        ),
        migrations.AlterField(
            model_name='items',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 11, 4, 4, 813011)),
        ),
        migrations.AlterField(
            model_name='items',
            name='order_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 18, 11, 4, 4, 813011)),
        ),
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 18, 11, 4, 4, 810004)),
        ),
    ]

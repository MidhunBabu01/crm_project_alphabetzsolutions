# Generated by Django 3.2.9 on 2022-01-05 05:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0063_auto_20220101_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 11, 27, 32, 744056)),
        ),
        migrations.AlterField(
            model_name='items',
            name='order_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 5, 11, 27, 32, 744056)),
        ),
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 5, 11, 27, 32, 744056)),
        ),
        migrations.CreateModel(
            name='Quotation_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotation_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_app.customer')),
            ],
        ),
    ]

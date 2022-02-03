# Generated by Django 3.2.9 on 2022-02-02 11:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0087_auto_20220202_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 4, 16, 45, 10, 351519)),
        ),
        migrations.AlterField(
            model_name='items',
            name='order_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 16, 45, 10, 351519)),
        ),
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 2, 2, 16, 45, 10, 348521)),
        ),
        migrations.RemoveField(
            model_name='leads',
            name='tools',
        ),
        migrations.AddField(
            model_name='leads',
            name='tools',
            field=models.ManyToManyField(blank=True, null=True, to='crm_app.Tools'),
        ),
    ]

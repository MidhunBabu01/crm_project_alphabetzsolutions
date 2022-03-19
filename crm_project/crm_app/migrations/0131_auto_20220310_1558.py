# Generated by Django 3.2.9 on 2022-03-10 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0130_auto_20220310_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 9, 15, 58, 8, 179171)),
        ),
        migrations.AlterField(
            model_name='items',
            name='order_Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 10, 15, 58, 8, 179171)),
        ),
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 10, 15, 58, 8, 174174)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, choices=[('High', 'High'), ('Highest', 'Highest'), ('Low', 'Low'), ('Lowest', 'Lowest')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('Not Stared', 'Not Started'), ('Deferred', 'Deferred'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Waiting For Approval', 'Waiting For Approval')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='subjects',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
# Generated by Django 3.2.9 on 2022-03-07 04:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools_management_app', '0020_alter_itemss_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemss',
            name='order_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 7, 10, 13, 59, 386246), null=True),
        ),
    ]

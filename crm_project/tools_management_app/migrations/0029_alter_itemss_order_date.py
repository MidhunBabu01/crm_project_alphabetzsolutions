# Generated by Django 3.2.9 on 2022-03-09 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools_management_app', '0028_alter_itemss_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemss',
            name='order_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 9, 15, 7, 40, 575022), null=True),
        ),
    ]

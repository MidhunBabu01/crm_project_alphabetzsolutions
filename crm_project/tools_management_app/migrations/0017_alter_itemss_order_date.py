# Generated by Django 3.2.9 on 2022-03-03 04:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools_management_app', '0016_alter_itemss_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemss',
            name='order_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 3, 10, 29, 18, 53016), null=True),
        ),
    ]
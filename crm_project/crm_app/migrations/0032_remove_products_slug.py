# Generated by Django 3.2.9 on 2021-12-10 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0031_products_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='slug',
        ),
    ]

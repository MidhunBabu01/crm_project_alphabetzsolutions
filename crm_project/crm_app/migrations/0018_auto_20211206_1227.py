# Generated by Django 3.2.9 on 2021-12-06 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0017_alter_customer_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='last_transaction',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='customer',
            name='total_transaction',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
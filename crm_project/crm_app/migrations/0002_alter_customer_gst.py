# Generated by Django 3.2.9 on 2021-12-03 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gst',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-03 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0005_alter_customer_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='photo',
            new_name='image',
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-18 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc_section', '0002_auto_20211217_1757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extendedusermodel',
            old_name='acompany_address',
            new_name='company_address',
        ),
    ]

# Generated by Django 3.2.9 on 2022-03-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc_section', '0006_auto_20220305_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedusermodel',
            name='is_staff2',
            field=models.BooleanField(default=False, verbose_name='is_staff2'),
        ),
        migrations.AlterField(
            model_name='extendedusermodel',
            name='is_superviser',
            field=models.BooleanField(default=False, verbose_name='is_superviser'),
        ),
    ]

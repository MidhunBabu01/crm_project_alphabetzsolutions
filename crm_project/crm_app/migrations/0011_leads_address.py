# Generated by Django 3.2.9 on 2021-12-04 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0010_alter_leads_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='address',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]

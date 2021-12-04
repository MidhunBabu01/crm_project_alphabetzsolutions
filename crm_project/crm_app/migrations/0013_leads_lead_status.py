# Generated by Django 3.2.9 on 2021-12-04 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0012_quotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='lead_status',
            field=models.CharField(choices=[('junk_leads', 'junk_leads'), ('open_leads', 'open_leads'), ('junk_leads', 'junk_leads')], default=1, max_length=25),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-04 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0011_leads_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodt_rate', models.IntegerField()),
                ('gst', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='pictures')),
            ],
        ),
    ]

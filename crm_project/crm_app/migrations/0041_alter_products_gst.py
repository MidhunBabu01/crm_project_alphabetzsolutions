# Generated by Django 3.2.9 on 2021-12-11 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0040_items_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='gst',
            field=models.IntegerField(choices=[('5', '5'), ('12', '12'), ('18', '18'), ('28', '28')]),
        ),
    ]
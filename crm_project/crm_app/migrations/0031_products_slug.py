# Generated by Django 3.2.9 on 2021-12-10 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0030_alter_products_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
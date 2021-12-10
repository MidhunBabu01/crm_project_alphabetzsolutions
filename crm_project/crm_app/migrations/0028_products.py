# Generated by Django 3.2.9 on 2021-12-10 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0027_auto_20211209_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('brand', models.CharField(max_length=25)),
                ('photo', models.ImageField(upload_to='products')),
                ('desc', models.TextField()),
                ('hsn', models.CharField(max_length=25)),
                ('qty', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('gst', models.CharField(choices=[('5%', '5%'), ('12%', '12%'), ('18%', '18%'), ('28%', '28%')], max_length=250)),
            ],
        ),
    ]

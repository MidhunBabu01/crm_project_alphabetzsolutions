# Generated by Django 3.2.9 on 2021-12-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0035_auto_20211210_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(max_length=50, unique=True)),
                ('Date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

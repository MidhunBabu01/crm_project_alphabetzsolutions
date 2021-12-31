# Generated by Django 3.2.9 on 2021-12-30 09:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0060_auto_20211230_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 12, 30, 14, 47, 47, 34314)),
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('order_Date', models.DateTimeField(default=datetime.datetime(2021, 12, 30, 14, 47, 47, 34314))),
                ('due_date', models.DateTimeField(default=datetime.datetime(2022, 1, 29, 14, 47, 47, 34314))),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_app.cartlist')),
                ('prodt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm_app.products')),
            ],
        ),
    ]
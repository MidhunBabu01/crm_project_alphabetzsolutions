# Generated by Django 3.2.9 on 2021-12-10 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0038_rename_item_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
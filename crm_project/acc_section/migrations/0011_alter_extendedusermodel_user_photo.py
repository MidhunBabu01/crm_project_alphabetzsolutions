# Generated by Django 3.2.9 on 2022-03-08 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc_section', '0010_extendedusermodel_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedusermodel',
            name='user_photo',
            field=models.ImageField(blank=True, null=True, upload_to='user'),
        ),
    ]
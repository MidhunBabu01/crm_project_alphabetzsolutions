# Generated by Django 3.2.9 on 2021-12-17 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc_section', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedusermodel',
            name='acompany_address',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extendedusermodel',
            name='comapny_name',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extendedusermodel',
            name='dob',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extendedusermodel',
            name='gst',
            field=models.IntegerField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='extendedusermodel',
            name='title',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-16 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0045_rename_testuser_testt'),
    ]

    operations = [
        migrations.CreateModel(
            name='TesttUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Testt',
        ),
    ]
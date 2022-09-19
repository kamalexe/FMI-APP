# Generated by Django 4.0.6 on 2022-09-17 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmiapp', '0005_logininfo_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerinfo',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='farmerinfo',
            name='userid',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='farmerinfo',
            name='usertype',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='merchantinfo',
            name='password',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='merchantinfo',
            name='userid',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='merchantinfo',
            name='usertype',
            field=models.CharField(default='', max_length=50),
        ),
    ]
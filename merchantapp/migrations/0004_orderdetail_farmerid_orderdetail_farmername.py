# Generated by Django 4.0.6 on 2022-09-18 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchantapp', '0003_orderdetail_merchantid_orderdetail_merchantname'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='farmerId',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='farmerName',
            field=models.CharField(default='', max_length=10),
        ),
    ]

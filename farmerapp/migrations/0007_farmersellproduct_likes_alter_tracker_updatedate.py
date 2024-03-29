# Generated by Django 4.0.6 on 2022-09-25 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmiapp', '0011_alter_farmerinfo_userid_alter_merchantinfo_userid'),
        ('farmerapp', '0006_alter_tracker_orderid_alter_tracker_orderstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmersellproduct',
            name='likes',
            field=models.ManyToManyField(related_name='FarmerSellProduct', to='fmiapp.merchantinfo'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='updateDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 25, 14, 13, 49, 490810)),
        ),
    ]

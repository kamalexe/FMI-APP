# Generated by Django 4.0.6 on 2022-10-08 08:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchantapp', '0006_orderdetail_productid'),
        ('farmerapp', '0035_alter_tracker_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='orderId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='merchantapp.orderdetail'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='updateDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 8, 14, 16, 1, 353956)),
        ),
    ]

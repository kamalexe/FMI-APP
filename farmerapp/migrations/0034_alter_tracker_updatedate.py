# Generated by Django 4.0.6 on 2022-10-07 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmerapp', '0033_alter_tracker_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='updateDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 10, 7, 19, 56, 10, 994100)),
        ),
    ]

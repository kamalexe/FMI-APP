# Generated by Django 4.0.6 on 2022-09-27 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irrigreatapp', '0007_smuserprofile_image_alter_smuser_creatdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smuser',
            name='creatDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 27, 20, 12, 5, 260189)),
        ),
        migrations.AlterField(
            model_name='smuser',
            name='updateDate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 27, 20, 12, 5, 260189)),
        ),
        migrations.AlterField(
            model_name='smuserprofile',
            name='creatDate',
            field=models.DateTimeField(blank=True, default='datetime.now()'),
        ),
        migrations.AlterField(
            model_name='smuserprofile',
            name='image',
            field=models.ImageField(default='', upload_to='irrigreatapp/images'),
        ),
        migrations.AlterField(
            model_name='smuserprofile',
            name='updateDate',
            field=models.DateTimeField(blank=True, default='datetime.now()'),
        ),
    ]

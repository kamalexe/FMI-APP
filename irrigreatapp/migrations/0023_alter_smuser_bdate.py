# Generated by Django 4.0.6 on 2022-10-07 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irrigreatapp', '0022_alter_smuserprofile_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smuser',
            name='bdate',
            field=models.DateTimeField(blank=True),
        ),
    ]

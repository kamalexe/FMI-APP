# Generated by Django 4.0.6 on 2022-09-29 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irrigreatapp', '0011_alter_smuserprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='smuserprofile',
            name='follow',
            field=models.ManyToManyField(related_name='follower', to='irrigreatapp.smuser'),
        ),
    ]
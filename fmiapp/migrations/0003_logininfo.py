# Generated by Django 4.1 on 2022-08-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmiapp', '0002_merchantinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('userid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]

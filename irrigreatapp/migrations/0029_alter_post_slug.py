# Generated by Django 4.0.6 on 2022-10-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irrigreatapp', '0028_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=20),
        ),
    ]

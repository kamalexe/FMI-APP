# Generated by Django 4.0.6 on 2022-10-05 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('irrigreatapp', '0017_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blogger_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='irrigreatapp.smuserprofile'),
        ),
    ]

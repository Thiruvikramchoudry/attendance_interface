# Generated by Django 4.1.7 on 2023-04-14 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symbiote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence_area',
            name='Time',
            field=models.TimeField(default=datetime.time(21, 29, 49, 811096)),
        ),
    ]

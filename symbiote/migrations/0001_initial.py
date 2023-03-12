# Generated by Django 4.1.7 on 2023-03-12 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='absenteism_count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=datetime.date(2023, 3, 12))),
                ('Total_person', models.IntegerField(default=0, null=True)),
                ('absent_count', models.IntegerField(default=0, null=True)),
                ('late_count', models.IntegerField(default=0, null=True)),
                ('preleave_count', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='attendence_area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_id', models.IntegerField()),
                ('Date', models.DateField(default=datetime.date(2023, 3, 12))),
                ('Time', models.TimeField(default=datetime.time(16, 56, 18, 809679))),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_name', models.CharField(max_length=40)),
                ('Employee_id', models.IntegerField()),
                ('Employee_age', models.IntegerField()),
                ('Employee_gender', models.CharField(max_length=6)),
            ],
        ),
    ]

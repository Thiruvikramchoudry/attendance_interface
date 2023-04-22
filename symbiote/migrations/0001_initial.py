# Generated by Django 4.1.7 on 2023-04-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=40)),
                ('employee_id', models.IntegerField()),
                ('employee_age', models.IntegerField()),
                ('employee_gender', models.CharField(max_length=6)),
                ('employee_location', models.CharField(max_length=100)),
                ('aadhar_card', models.IntegerField()),
                ('working_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.IntegerField()),
                ('project_area', models.CharField(max_length=100)),
                ('employee_required', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='supervisor_assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor_name', models.CharField(max_length=100)),
                ('assign_work_at', models.IntegerField()),
                ('employee_list', models.FileField(upload_to='employee_assign')),
            ],
        ),
        migrations.CreateModel(
            name='supervisor_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supervisor_name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]

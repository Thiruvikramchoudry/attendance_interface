# Generated by Django 4.1.7 on 2023-04-23 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symbiote', '0004_remove_supervisor_assign_assign_work_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee_assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('project_id', models.IntegerField()),
            ],
        ),
    ]

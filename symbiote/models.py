from django.db import models
import datetime

# Create your models here.

class employee_details(models.Model):
    employee_name=models.CharField(max_length=40)
    employee_id=models.IntegerField()
    employee_age=models.IntegerField()
    employee_gender=models.CharField(max_length=6)
    employee_location=models.CharField(max_length=100)
    aadhar_card=models.IntegerField()
    working_status=models.BooleanField(default=False)

    def __str__(self):
        return self.employee_name

class employee_assign(models.Model):
    employee_id=models.IntegerField()
    project_id=models.IntegerField()

    def __str__(self):
        return str(self.employee_id)



class supervisor_assign(models.Model):
    supervisor_username=models.CharField(max_length=100)
    project_id=models.IntegerField()

    employee_list=models.FileField(upload_to='employee_assign')

    def __str__(self):
        return str(self.supervisor_username)

class supervisor_detail(models.Model):
    supervisor_name=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return str(self.supervisor_name)

class project(models.Model):
    project_id=models.IntegerField()
    project_area=models.CharField(max_length=100)
    employee_required=models.IntegerField()
    status=models.CharField(max_length=100,default="Not Started")
    supervisor=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    from_date=models.DateField()
    to_date=models.DateField()

    def __str__(self):
        return str(self.project_id)









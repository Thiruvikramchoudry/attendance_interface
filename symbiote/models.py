from django.db import models
import datetime

# Create your models here.

class details(models.Model):
    Employee_name=models.CharField(max_length=40)
    Employee_id=models.IntegerField()
    Employee_age=models.IntegerField()
    Employee_gender=models.CharField(max_length=6)


    def __str__(self):
        return self.Employee_name

class attendence_area(models.Model):
    employee_id=models.IntegerField()
    date=models.CharField(max_length=40,default=str(datetime.date.today()))
    time=models.CharField(max_length=40,default=str(datetime.datetime.now().time()))

    def __str__(self):
        return str(self.employee_id)


class absenteism_count(models.Model):
    Date=models.DateField(default=datetime.date.today())
    Total_person=models.IntegerField(null=True,default=0)
    absent_count=models.IntegerField(null=True,default=0)
    late_count=models.IntegerField(null=True,default=0)
    preleave_count=models.IntegerField(null=True,default=0)

    def __str__(self):
        return str(self.Date)




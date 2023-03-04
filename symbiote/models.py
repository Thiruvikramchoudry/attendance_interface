from django.db import models

# Create your models here.

class details(models.Model):
    Employee_name=models.CharField(max_length=40)
    Status=models.CharField(max_length=1000)

    def __str__(self):
        return self.Employee_name


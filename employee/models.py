from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=120,primary_key=True)
    employee_name=models.CharField(max_length=120)
    designation=models.CharField(max_length=120)
    Salary=models.PositiveIntegerField()
    Email=models.EmailField(unique=True)
    experience=models.PositiveIntegerField(null=True)

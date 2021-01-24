from django.db import models

class EmployeeDetails(models.Model):
    emp_identity = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    department = models.CharField(max_length=100)
    hire_date = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=100)

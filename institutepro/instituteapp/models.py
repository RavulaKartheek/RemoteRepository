from django.db import models

class ContactData(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    comment = models.CharField(max_length=100)

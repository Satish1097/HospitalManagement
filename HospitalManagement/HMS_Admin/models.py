from django.db import models

# Create your models here.

class Admin(models.Model):
    AdminId=models.CharField(max_length=50)
    Password=models.CharField(max_length=18)
    def __str__(self):
        return self.AdminId

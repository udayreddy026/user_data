from django.db import models

# Create your models here.

class user(models.Model):
    id = models.BigAutoField(primary_key=True)
    first = models.CharField(max_length=40) 
    last = models.CharField(max_length=40)
    email= models.CharField(max_length=40)
    dob = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    class Meta:
      db_table = "user"
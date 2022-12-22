from django.db import models

# Create your models here.

class Person(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField(max_length=3)
    mail=models.EmailField(max_length=50)
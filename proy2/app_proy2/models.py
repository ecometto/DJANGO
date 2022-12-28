from django.db import models
from datetime import datetime
# Create your models here.

class Personas(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha_carga=models.DateTimeField()




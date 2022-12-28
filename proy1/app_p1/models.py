from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.TextField(max_length=50)
    mail = models.EmailField(max_length=50)
    passw = models.TextField(max_length=50)

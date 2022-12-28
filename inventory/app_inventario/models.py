from django.db import models
from django.utils.timezone import now

# Create your models here.

class Umedida(models.Model):
    unidad = models.CharField (max_length=50) 
    
    def __str__(self):
        return self.unidad
    
    
class Articulos(models.Model):
    descripcion=models.CharField(max_length=50)
    umedida=models.ForeignKey(Umedida, on_delete=models.CASCADE)
    detalles=models.CharField(max_length=200)
    cantidad= models.IntegerField(default=0)
    
    def __str__(self):
        return self.descripcion


class Movimientos1(models.Model):
    fechaMov=models.DateField(default=now, blank=False)
    tipoMov=models.CharField(max_length=50, blank=False, choices=(("ingreso","ingreso"), ("egreso", "egreso")))

    detallesMov=models.CharField(max_length=300, blank=False)
    artId=models.ForeignKey(Articulos, on_delete=models.PROTECT, blank=False)
    cantidadMov=models.IntegerField(blank=False)

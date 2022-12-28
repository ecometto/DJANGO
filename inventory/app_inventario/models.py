from django.db import models

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
    
    # def __str__(self):
    #     return self.descripcion
    
class Movimientos(models.Model):
    item=models.PositiveSmallIntegerField()
    art_id = models.ForeignKey(Articulos, on_delete=models.CASCADE)    
    tipo_movimiento = models.CharField(max_length=50, blank=False)
    


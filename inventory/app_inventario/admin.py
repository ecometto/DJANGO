from django.contrib import admin

from app_inventario.models import Articulos, Movimientos1
# Register your models here.


# @admin.register(Articulos)
# class ArticulosAdmin(admin.ModelAdmin):
#     list_display = ('descripcion', 'umedida', 'detalles')
#     list_filter = ('umedida',)
#     ordering = ('descripcion',)
#     search_fields = ('descripcion',)

admin.site.register(Movimientos1, list_display=("fechaMov", "tipoMov", "artId", "cantidadMov"))
admin.site.register(Articulos, list_display = ('descripcion', 'umedida', 'detalles'))


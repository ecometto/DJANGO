from django.contrib import admin

from app_inventario.models import Articulos
# Register your models here.


@admin.register(Articulos)
class ArticulosAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'umedida', 'detalles')
    list_filter = ('umedida',)
    ordering = ('descripcion',)
    search_fields = ('descripcion',)
    
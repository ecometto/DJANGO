from django.contrib import admin
from .models import Usuarios

# Register your models here.

class Usuarios_admin(admin.ModelAdmin):
    list_display = ('nombre', 'mail')
    search_fields = ('nombre','mail')
    
admin.site.register(Usuarios, Usuarios_admin)

from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import sqlite3

from app_inventario.models import Articulos
# Create your views here.

def index(request):
    return render(request, 'index.html', {"titulo":"principal"})


def articulos(request):
    if request.method == "POST":
        desc=request.POST['descripcion']
        umedida=request.POST['umedida']
        det=request.POST['detalles']
        cant=request.POST['cantidad']
        art=Articulos.objects.create(descripcion=desc, detalles=det, cantidad=cant, umedida_id=umedida)
    
    articulos = Articulos.objects.all() 
    context={
        "titulo":"ABM- Articulos", 
        "data":articulos
    }
    return render(request, 'articulos.html', context)


def movimientos(request):
    articulos = Articulos.objects.all()
    context={
        "titulo":"movimientos",
        "articulos":articulos
    }
    return render(request, 'movimientos.html', context)

def listados(request):
    return render(request, 'listados.html', {"titulo":"listados"})

# funciones de ARTICULOS ---------------------
#Ver. Se incluyen en URLS.py
def art_edit(request, id):
    if request.method == 'POST':
        id=request.POST['id']
        desc=request.POST['descripcion']
        det=request.POST['detalles']
        um=request.POST['umedida']
        cant=request.POST['cantidad']

        ax=Articulos.objects.get(id=id)
        ax.descripcion= desc
        ax.detalles=det
        ax.umedida_id=um
        ax.save()        
        return redirect(articulos)
    
    art_to_edit = Articulos.objects.get(id=id)
    context = {
        "titulo":"Editing..",
        "data" : art_to_edit,
        "unidad" : int(art_to_edit.umedida_id)
        }
    return render(request, 'art_edit.html', context)
  

def art_delete(request, id):
    art_to_del = Articulos.objects.get(id=id)
    art_to_del.delete()
    return redirect(articulos)




       
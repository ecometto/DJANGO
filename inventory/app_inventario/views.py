from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.db.models import Max
from datetime import datetime
import sqlite3

from app_inventario.models import Umedida, Articulos, Movimientos1
# Create your views here.

def index(request):
    return render(request, 'index.html', {"titulo":"principal"})

# funciones de ARTICULOS ---------------------
#Ver. Se incluyen en URLS.py
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
    print(art_to_del.descripcion)
    art_to_del.delete()
    return redirect(articulos)


# funciones de MOVIMIENTOS ---------------------
def movimientos(request):
    ultimoMov=Movimientos1.objects.all().aggregate(Max('id'))
    if ultimoMov['id__max'] == None:
        ultimoMov = 0
    else:
        ultimoMov= ultimoMov['id__max']
        
    fecha=datetime.now().strftime("%d/%m/%Y")
    articulos = Articulos.objects.all()
    context={
        "titulo":"movimientos",
        "ultimoMov":ultimoMov,
        "fecha":fecha,
        "articulos":articulos
    }
    return render(request, 'movimientos.html', context)

def getOneArticle(request, id):
    # art=Articulos.objects.filter(id=id).values('id','descripcion','umedida_id', 'umedida')  
    art=Articulos.objects.filter(id=id).values()
    umedida=art[0]['umedida_id']
    umedida_text = Umedida.objects.get(id=umedida)
    
    print("------------------------------------------")
    print(umedida_text)
    # for obj in art:
    #         print(obj['id'])

    lista=list(art)
    print(lista)

    return JsonResponse({"articulo":lista[0], "umedida":f"{umedida_text}"})




def listados(request):
    return render(request, 'listados.html', {"titulo":"listados"})
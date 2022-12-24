from django.shortcuts import render
import sqlite3

# con=sqlite3.connect('db.sqlite3')
# cur=con.cursor()
# sql="select * from app_inventario_articulos"
# cur.execute(sql)
# data=cur.fetchall()
# print(data)
# print(type(data))
# con.close()



from app_inventario.models import Articulos
# Create your views here.

def index(request):
    return render(request, 'index.html', {"titulo":"principal"})


def articulos(request):
    articulos = Articulos.objects.all()

 

    return render(request, 'articulos.html', {"titulo":"ABM- Articulos", "data":data})


def movimientos(request):
    return render(request, 'movimientos.html', {"titulo":"movimientos"})

def listados(request):
    return render(request, 'listados.html', {"titulo":"listados"})
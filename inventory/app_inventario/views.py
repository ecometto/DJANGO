from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html', {"titulo":"principal"})


def articulos(request):
    return render(request, 'articulos.html', {"titulo":"ABM- Articulos"})


def movimientos(request):
    return render(request, 'movimientos.html', {"titulo":"movimientos"})

def listados(request):
    return render(request, 'listados.html', {"titulo":"listados"})
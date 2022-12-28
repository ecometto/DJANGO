
from django.shortcuts import render, redirect
from django.http import HttpResponse  
import datetime

from .models import Personas
# Create your views here.

def index (request):
    lista=Personas.objects.all()
    return render(request, 'index.html', {"titulo":"mytitle", "lista":lista})

def cargar(request):
    if request.method=="POST":
        nom=request.POST['nombre']
        ape=request.POST['apellido']
        ed=request.POST['edad']
        agregar=Personas.objects.create(nombre=nom, apellido=ape, edad=ed, fecha_carga=datetime.datetime.now())
        return redirect('/')
    else:
        return HttpResponse("error en el methodo")

def services (request):
    return render(request, 'services.html')

def contact (request):
    return render(request, 'contact.html')
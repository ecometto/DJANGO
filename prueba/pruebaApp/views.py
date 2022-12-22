from django.shortcuts import render
from django.http import HttpResponse

from .models import Alumnos


# Create your views here.

def index(request):
    lista = Alumnos.objects.all()
    # return HttpResponse('hola')
    return render(request,'index.html', {"lista":lista})
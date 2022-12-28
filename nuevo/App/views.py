from django.shortcuts import render
from .models import Person
# Create your views here.

def index(request):
    data = Person.objects.all()
    return render(request, 'index.html', {"data":data})

def indexID(request, ide):
    data = Person.objects.get(id=ide)
    print(data.nombre)
    return render(request, 'index2.html', {"data":data})
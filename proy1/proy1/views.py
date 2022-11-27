from django.http import HttpResponse    
from datetime import datetime


def saludo(request, nombre, edad):
    return HttpResponse(f"hola hola {nombre}. \nTu edad es {edad}")

def despedida(request, nombre, edad):
    return HttpResponse(f"hasta la vista {nombre}. \nTu edad es {edad}")

def fecha(request):
    return HttpResponse(f"la fecha y hor aactual es: {datetime.now()}")

def edad(request, edad, anio):
    actualYear=datetime.now().year
    edadFutura=(anio-actualYear) + edad
    return HttpResponse("Si tu edad hoy ( %s ) es de : %s años, entonces en el año %s tendrás: %s" %(actualYear, edad, anio, edadFutura))
from django.http import HttpResponse
from datetime import datetime
from django.template import loader
from django.shortcuts import render


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
   
   
def pl_externa(request):   
    lista=['marta', 'rosa', 'miguel', 'juan', 'rodrigo']
    plantilla=loader.get_template("saludo.html")
    doc = plantilla.render({"lista":lista})
    return HttpResponse(doc)

def mes_numero_letra(mes_numero):
    mes_num=[1,2,3,4,5,6,7,8,9,10,11,12]
    mes_letras=['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre' ]
    for i in range(len(mes_num)):
        if mes_num[i] == mes_numero:
            mes=mes_letras[i]
    return mes

def fecha_actual(request):
    fecha= datetime.now()
    print('hello............')
    dia=fecha.day
    mes = mes_numero_letra(fecha.month)
    year=fecha.year
    plt=loader.get_template('fecha_actual.html')
    doc = plt.render({"dia":dia, "mes":mes, "anio": year})
    return HttpResponse(doc)

def advanceView(request):
    return render(request, 'advance.html', {"nombre": "Edgardo", "edad": 40} )



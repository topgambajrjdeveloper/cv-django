from django.shortcuts import render

# Create your views here.


def Inicio(request):
    from .models import Inicio, Servicios
    inicio = Inicio.objects.all()
    servicio = Servicios.objects.all()
    return render(request, "inicio.html", {'inicio': inicio, 'servicio': servicio})

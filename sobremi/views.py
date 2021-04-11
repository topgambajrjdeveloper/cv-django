from django.shortcuts import render

# Create your views here.


def SobreMi(request):
    from .models import Habilidades, Certificaciones, Experiencia, SobreMi
    about = SobreMi.objects.all()
    habilidad = Habilidades.objects.all()
    certificacion = Certificaciones.objects.all()
    experiencia = Experiencia.objects.all()
    return render(request, 'sobre-mi.html', {
        'habilidad': habilidad,
        'certificacion': certificacion,
        'experiencia': experiencia,
        'about': about
    })

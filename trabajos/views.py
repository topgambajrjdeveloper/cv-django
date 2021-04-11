from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Trabajos, Categoria
from django.views.generic import DetailView
# Create your views here.


def Jobs(request):
    job = Trabajos.objects.all()
    return render(request, 'trabajos.html', {'job': job})


def Categorias(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    job = Trabajos.objects.filter(categorias=categoria)
    return render(request, 'categorias.html', {'categoria': categoria, 'job': job})


class JobsDetalView(DetailView):
    model = Trabajos
    template_name = 'detail.html'

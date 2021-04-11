from django.db import models

# Create your models here.


class Inicio(models.Model):
    titulo = models.CharField(max_length=100)
    description = models.CharField(
        max_length=500)
    parrafo = models.CharField(
        max_length=500)
    github = models.CharField(max_length=500)
    linkendin = models.CharField(max_length=500)
    twitter = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "inicio"
        verbose_name_plural = "inicios"

    def __str__(self):
        return self.titulo


class Servicios(models.Model):
    #servicios
    icons = models.ImageField(upload_to='servicios/')
    titulo = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

from django.db import models

# Create your models here.


class SobreMi(models.Model):
    image = models.ImageField(upload_to='sobremi/')
    titulo = models.CharField(max_length=100)
    description = models.CharField(
        max_length=500)
    proyectos = models.IntegerField()
    clientes = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "sobremi"
        verbose_name_plural = "sobremis"

    def __str__(self):
        return self.titulo


class Habilidades(models.Model):
    # Habilidades
    titulo = models.CharField(max_length=200)
    lenguaje = models.CharField(max_length=200)
    percentaje = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "habilidad"
        verbose_name_plural = "habilidades"
        ordering = ["-created"]

    def __str__(self):
        return self.titulo


class Certificaciones(models.Model):
    # Cerificaciones
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    parafo = models.CharField(
        max_length=500)
    url = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "certificacion"
        verbose_name_plural = "certificaciones"
        ordering = ["-created"]

    def __str__(self):
        return self.titulo


class Experiencia(models.Model):
    # ResumenCerificaciones
    titulo = models.CharField(
        max_length=100)
    fecha = models.DateField()
    parafo = models.CharField(
        max_length=500)
    url = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "experiencia"
        verbose_name_plural = "experiencias"
        ordering = ["-created"]

    def __str__(self):
        return self.titulo

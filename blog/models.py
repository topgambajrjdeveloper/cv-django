from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.shortcuts import reverse
# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre


class Post(models.Model):
    thumbnails = models.ImageField(upload_to='blog/', null=True, blank=True)
    thumbnails_second = models.ImageField(
        upload_to='blog/', null=True, blank=True)
    image = models.ImageField(upload_to='blog/', null=True, blank=True)
    titulo = models.CharField(max_length=100)
    description = models.TextField(
        max_length=5000)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })

    @property
    def get_categories_count(self):
        return self.categorias.all().count()

    def __str__(self):
        return self.titulo


class PostView(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.timestamp


class Like(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.timestamp

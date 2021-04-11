from django.contrib import admin
from .models import Categoria, Post, PostView, Like

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", )
    search_fields = ["nombre"]
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", 'slug',)
    search_fields = ["titulo"]
    readonly_fields = ('created', 'updated')
    prepopulated_fields = {'slug': ('titulo',)}


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)

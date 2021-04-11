from django.contrib import admin
from inicio.models import Inicio, Servicios

# Register your models here.


class InicioAdmin(admin.ModelAdmin):
    list_display = ("titulo",)
    readonly_fields = ('created', 'updated')


class ServiciosAdmin(admin.ModelAdmin):
    list_display = ("titulo",)
    search_fields = ["titulo"]
    readonly_fields = ('created', 'updated')


admin.site.register(Inicio, InicioAdmin)
admin.site.register(Servicios, ServiciosAdmin)

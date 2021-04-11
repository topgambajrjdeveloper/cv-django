from django.contrib import admin
from .models import SobreMi, Experiencia, Habilidades, Certificaciones

# Register your models here.


class SobreMiAdmin(admin.ModelAdmin):
    list_display = ("titulo", )
    search_fields = ["titulo", "description"]
    readonly_fields = ('created', 'updated')


class HabilidadesAdmin(admin.ModelAdmin):
    list_display = ("titulo", "lenguaje")
    search_fields = ["titulo", "lenguaje"]
    readonly_fields = ('created', 'updated')


class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ("titulo", )
    search_fields = ["titulo"]
    readonly_fields = ('created', 'updated')


class CertificacionesAdmin(admin.ModelAdmin):
    list_display = ("titulo", )
    search_fields = ["titulo"]
    readonly_fields = ('created', 'updated')


admin.site.register(SobreMi, SobreMiAdmin)
admin.site.register(Habilidades, HabilidadesAdmin)
admin.site.register(Experiencia, ExperienciaAdmin)
admin.site.register(Certificaciones, CertificacionesAdmin)

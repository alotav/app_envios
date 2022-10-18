from django.contrib import admin

# Para agregar la aplicacion "Servicios" al panel administrador: registramos / importamos la aplicacion que creamos:
from .models import Servicio
# generamos una clase para los campós agregados automaticamente a la db:
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
# Register your models here.
admin.site.register(Servicio, ServicioAdmin)
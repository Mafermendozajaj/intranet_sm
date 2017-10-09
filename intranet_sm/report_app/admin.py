from django.contrib import admin
from .models import Proyecto, Reporte, Telescopio, Respuesta

#cambiar a Proyecto sin s
admin.site.register(Proyecto)
admin.site.register(Reporte)
admin.site.register(Telescopio)
admin.site.register(Respuesta)
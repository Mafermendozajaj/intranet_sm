from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .models import Vacacion, Permiso, Incidencia


admin.site.register(Vacacion)
admin.site.register(Permiso)
admin.site.register(Incidencia)

#@admin.register(Incidencia)
#class MyIncidenciaAdmin(UserAdmin):
#    pass



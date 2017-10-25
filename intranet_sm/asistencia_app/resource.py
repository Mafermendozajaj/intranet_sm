from import_export import resources, widgets

from intranet_sm.asistencia_app.models import Marca, Dispositivo
# from  EmpleadoClienteDispositivo, EmpleadoCliente
from import_export import fields


class MarcaResource(resources.ModelResource):
    nombre = fields.Field(column_name='Nombre Dispositivo',
                          attribute='dispositivo',
                          widget=widgets.ForeignKeyWidget(Dispositivo, 'nombre')
                          )

    ubicacion = fields.Field(column_name='Ubicacion Dispositivo',
                             attribute='dispositivo',
                             widget=widgets.ForeignKeyWidget(Dispositivo, 'ubicacion'))

    nombres = fields.Field()

    def dehydrate_nombres(self, marca):
        return marca.get_empleado_full_name()

    class Meta:
        model = Marca
        fields = ('id', 'id_user', 'nombre', 'fecha',)
        export_order = ('id', 'nombre', 'ubicacion', 'id_user', 'nombres', 'fecha')
        widgets = {
            'fecha': {'format': '%d/%m/%Y %H:%M'},
        }

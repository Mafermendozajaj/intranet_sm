from django.db import models
from intranet_sm.users.models import Empleado


TIPO_CONSTANCIA_CHOICES = (
    ('SS', 'Sin salario'),
    ('SN', 'Salario normal'),
    ('SB', 'Salario base'),
    ('SI', 'Salario integral'),
    ('SBV', 'Salario banavih'),
)

ESTADO_CONSTANCIA_CHOICES = (
    ('N', 'Nueva'),
    ('P', 'En proceso'),
    ('C', 'Completada'),
    ('E', 'Eliminada'),
    ('V', 'Vencida'),
)


class Constancia (models.Model):
    empleado = models.ForeignKey(Empleado)
    fecha_solicitud = models.DateField('Fecha de solicitud', auto_now_add=True)
    fecha_aprobacion = models.DateField('Fecha de aprobacion', auto_now_add=True)
    sueldo = models.FloatField('Salario', null=True, blank=True, default='0', help_text="Salario del empleado")
    tipo_constancia = models.CharField('Tipo de constancia', max_length=100, choices=TIPO_CONSTANCIA_CHOICES, default='Sin sueldo', help_text="Seleccione el tipo de constancia")
    estado_constancia = models.CharField('Estado de la constancia', max_length=15, choices=ESTADO_CONSTANCIA_CHOICES, default='Nueva', help_text="Seleccione el estado de la constancia")

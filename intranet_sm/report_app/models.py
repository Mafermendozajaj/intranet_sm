from django.db import models
from intranet_sm.users.models import Empleado


TIPO_REPORTE_CHOICES = (
    ('A', 'Reporte A'),
    ('B', 'Reporte B'),
    ('C', 'Reporte C'),
)

class Proyecto (models.Model):	
    proyecto = models.CharField('Proyecto',max_length=255)
    cod_proyecto = models.CharField(max_length=20)

    def __str__(self):
        return u'%s' % (self.proyecto)

class Telescopio(models.Model):
    telescopio = models.CharField('Telescopio',max_length=30)

    def __str__(self):
        return u'%s' % (self.telescopio)



class Reporte(models.Model):
    asistente = models.ForeignKey(Empleado)
    observador = models.CharField('Observador',max_length=100, null=True, blank=True)
    proyecto = models.ForeignKey(Proyecto)
    tipo_reporte = models.CharField('Tipo de reporte', max_length=2,choices=TIPO_REPORTE_CHOICES, default='A')
    telescopio = models.ForeignKey(Telescopio)
    fecha_obs = models.DateField('Fecha de observacion')
    datos = models.BooleanField(default=True)
    observadores = models.CharField('Observadores', max_length=100, null=True, blank=True, default='', help_text="Introduzca los nombres de los observadores")
    horas_trabajadas = models.IntegerField()
    hp_clima = models.DecimalField('HP Clima', max_digits=4, decimal_places=2)
    hp_instrumentos = models.DecimalField('HP instrumentos', max_digits=4, decimal_places=2)
    hp_software = models.DecimalField('HP Software', max_digits=4, decimal_places=2)
    comentarios = models.TextField('Comentarios')
    vacio_camara = models.DecimalField('Vacio de cámara', max_digits=6, decimal_places=2)
    vacio_ls = models.DecimalField('Vacio de ls', max_digits=6, decimal_places=2)
    vacio_li = models.DecimalField('Vacio de li', max_digits=6, decimal_places=2)
    enviado = models.BooleanField(default=False)
    fecha_reg = models.DateField('Fecha de registro', auto_now_add=True)
    ult_act = models.DateField('Ultima actualización', auto_now=True)


class Respuesta(models.Model):
    repuesta = models.TextField('Respuesta')
    reporte = models.ForeignKey(Reporte)
    fecha_reg = models.DateField('Fecha de registro', auto_now_add=True)

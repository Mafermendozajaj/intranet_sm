# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.db import models

from intranet_sm.users.models import Empleado


class Dispositivo(models.Model):
    ubicacion = models.CharField(max_length=200, default='ubicado en')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id) + ' ubicado en: ' + self.ubicacion

    def get_ubicacion(self):
        ubicacion = '%s' % (self.ubicacion)
        return ubicacion


class EmpleadoClienteDispositivo(models.Model):
    dispositivo = models.ForeignKey(Dispositivo)
    empleado = models.ForeignKey(Empleado)
    id_user = models.IntegerField()

    def get_empleado_full_name(self):
        dc = EmpleadoClienteDispositivo.objects.get(id_user=self.id_user, dispositivo=self.dispositivo)
        full_name = '%s, %s' % (dc.empleado.nombre, dc.empleado.apellidos)
        return full_name

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ('dispositivo', 'empleado')


class Marca(models.Model):
    id_user = models.IntegerField(default=1)
    dispositivo = models.ForeignKey(Dispositivo)
    title = models.CharField(max_length=10, default='Entrada')
    start = models.DateTimeField()

    def get_empleado_full_name(self):
        dc = EmpleadoClienteDispositivo.objects.get(id_user=self.id_user, dispositivo=self.dispositivo)
        full_name = '%s, %s' % (dc.empleado.first_name, dc.empleado.last_name)
        return full_name

    def get_empleado_id(self):
        dc = EmpleadoClienteDispositivo.objects.get(id_user=self.id_user, dispositivo=self.dispositivo)
        return int(dc.empleado.id)

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = ('id_user', 'dispositivo', 'start',)
        ordering = ('-start',)


class Incidencia(models.Model):
    title = models.CharField(max_length=250)
    start = models.DateTimeField()
    end = models.DateTimeField()


class Nota(models.Model):
    empleado = models.ForeignKey(Empleado, default=1)
    title = models.CharField(max_length=250)
    start = models.DateTimeField()
    end = models.DateTimeField()


class Permiso(models.Model):
    user = models.ForeignKey(Empleado)
    title = models.CharField(max_length=250)
    start = models.DateTimeField()
    end = models.DateTimeField()
    fecha_act = models.DateTimeField(auto_now=True, blank=True)
    fecha_reg = models.DateTimeField(auto_now_add=True)


class Vacacion(models.Model):
    user = models.ForeignKey(Empleado)
    nro_dias = models.IntegerField(default=0)
    fecha_act = models.DateTimeField(auto_now=True, blank=True)
    fecha_reg = models.DateTimeField(auto_now_add=True, blank=True)


class VacacionSolicitud(models.Model):
    user = models.ForeignKey(Empleado)
    title = models.CharField(max_length=250)
    start = models.DateTimeField()
    end = models.DateTimeField()
    nro_dias = models.IntegerField(default=0)
    aprobada = models.BooleanField(default=False)
    solicita_bono_vacacional = models.BooleanField(default=False)
    fecha_reincorporacion = models.DateField()
    fecha_act = models.DateTimeField(auto_now=True, blank=True)
    fecha_reg = models.DateTimeField(auto_now_add=True, blank=True)
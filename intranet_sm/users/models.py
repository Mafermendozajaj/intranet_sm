# -*- coding: utf-8 -*-
import datetime

from dateutil import relativedelta
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField


GENERO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

NACIONALIDAD_CHOICES = (
    ('V', 'Venezolano'),
    ('E', 'Extranjero'),
)

ESTADO_CHOICES = (
    ('A', 'Activo'),
    ('R', 'Retirado'),
    ('J', 'Jubilado'),
    ('P', 'Pencionado'),
)

TIPO_PERSONAL_CHOICES = (
    ('E', 'Empleado'),
    ('O', 'Obrero'),
    ('S', 'Estudiante'),
)

DATE_INPUT_FORMATS = ('%d-%m-%Y')


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})


@python_2_unicode_compatible
class Departamento(models.Model):
    departamento = models.CharField(max_length=80)

    def __str__(self):
        return self.departamento


@python_2_unicode_compatible
class Empleado(User):
    nacionalidad = models.CharField(max_length=16, choices=NACIONALIDAD_CHOICES, default='V')
    cedula = models.CharField('cédula de identidad', max_length=8, unique=True)
    departamento = models.ForeignKey(Departamento, db_index=True, default=1)
    cargo = models.CharField('Cargo', max_length=100, null=True, blank=True, default='')
    genero = models.CharField('género', max_length=16, choices=GENERO_CHOICES, default='M')
    fechaNacimiento = models.DateField('fecha de nacimiento', default=datetime.date.today)
    fechaIngreso = models.DateField('fecha de ingreso', default=datetime.date.today)
    fechaEgreso = models.DateField('fecha de egreso', null=True, blank=True, default='1900-01-01')
    direccion = models.TextField('dirección de habitación', blank=True, max_length=128, default='')
    telefonoCelular = models.CharField('Teléfono', max_length=16, null=True, blank=True, default='')
    estado = models.CharField(max_length=16, choices=ESTADO_CHOICES, default='A')
    tipo_personal = models.CharField(max_length=16, choices=TIPO_PERSONAL_CHOICES, default='E')
    foto = ThumbnailerImageField(
        upload_to="foto_perfiles/",
        default='none',
        help_text='recomendado 120px x 120px png o jpg'
    )
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'perfil de usuario'
        verbose_name_plural = 'perfiles de usuario'
        ordering = ('last_name', 'first_name',)

    def __str__(self):
        #return self.last_name
        return u"%s" % self.last_name + ', ' + self.first_name

    @property
    def edad(self):
        retorno = None
        hoy = datetime.date.today()
        if self.fechaNacimiento:
            retorno = u"%s" % relativedelta.relativedelta(hoy, self.fechaNacimiento).years
        return retorno

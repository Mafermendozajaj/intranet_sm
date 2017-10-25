# -*- coding: utf-8 -*-
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from pure_pagination.mixins import PaginationMixin

from intranet_sm.asistencia_app.models import Dispositivo


class DispositivoMixin(object):
    model = Dispositivo


class DispositivoList(GroupRequiredMixin, DispositivoMixin, PaginationMixin,
                      ListView):
    # required
    group_required = u"Administrador"
    raise_exception = True

    template_name = 'asistencia_app/dispositivos/object_list.html'

    page = {
        'title': 'Dispositivos',
        'subtitle': 'listado'
    }

    def get_context_data(self, **kwargs):
        context = super(DispositivoList, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class DispositivoDetatil(DispositivoMixin, DetailView):
    pass


class DispositivoCreate(GroupRequiredMixin, DispositivoMixin,
                        SuccessMessageMixin, CreateView):
    # required
    group_required = u"Administrador"
    raise_exception = True

    template_name = 'asistencia_app/dispositivos/object_form.html'
    success_url = reverse_lazy('dispositivo_list')
    success_message = "Dispositivo registrado satisfactoriamente"
    fields = ['id', 'ubicacion', 'activo']

    page = {
        'title': 'Dispositivos',
        'subtitle': 'agregar'
    }

    def get_context_data(self, **kwargs):
        context = super(DispositivoCreate, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class DispositivoUpdate(GroupRequiredMixin, DispositivoMixin,
                        SuccessMessageMixin, UpdateView):
    # required
    group_required = u"Administrador"
    raise_exception = True

    template_name = 'asistencia_app/dispositivos/object_form.html'
    success_url = reverse_lazy('dispositivo_list')
    success_message = "Dispositivo actualizado satisfactoriamente"
    fields = ['id', 'ubicacion', 'activo']

    page = {
        'title': 'Dispositivos',
        'subtitle': 'actualización'
    }

    def get_context_data(self, **kwargs):
        context = super(DispositivoUpdate, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class DispositivoDelete(GroupRequiredMixin, DispositivoMixin,
                        SuccessMessageMixin, DeleteView):
    # required
    group_required = u"Administrador"
    raise_exception = True

    template_name = 'asistencia_app/dispositivos/object_confirm_delete.html'
    success_message = "Dispositivo eliminado satisfactoriamente"
    success_url = reverse_lazy('dispositivo_list')

    page = {
        'title': 'Dispositivos',
        'subtitle': 'eliminación'
    }

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DispositivoDelete, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DispositivoDelete, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

# -*- coding: utf-8 -*-
from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from pure_pagination.mixins import PaginationMixin

from intranet.asistencia_app.models import Dispositivo


class DispositivoMixin(object):
    model = Dispositivo


class DispositivoList(GroupRequiredMixin, DispositivoMixin, PaginationMixin,
                      ListView):
    # required
    group_required = u"Administrador"
    raise_exception = True

    template_name = 'registros_app/dispositivos/object_list.html'

    page = {
        'title': 'Dispositivos',
        'subtitle': 'listado'
    }

    def get_context_data(self, **kwargs):
        context = super(DispositivoList, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

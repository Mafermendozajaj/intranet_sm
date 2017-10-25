# -*- coding: utf-8 -*-

from braces.views import GroupRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from pure_pagination.mixins import PaginationMixin

from intranet_sm.asistencia_app.models import Dispositivo, Marca, EmpleadoClienteDispositivo


class EmpresaDispositivoList(PaginationMixin, ListView):
    # required
    #group_required = u"Empresa"
    #raise_exception = True

    model = Dispositivo

    template_name = 'asistencia_app/dispositivos/object_list.html'

    page = {
        'title': 'Dispositivos de la CIDA',
        'subtitle': 'listado'
    }

    def get_context_data(self, **kwargs):
        context = super(EmpresaDispositivoList, self).get_context_data(**kwargs)
        context['page'] = self.page

        return context


class EmpresaDispositivoDetail(GroupRequiredMixin, DetailView):
    # required
    group_required = u"Empresa"
    raise_exception = True

    model = Dispositivo

    template_name = 'registros_app/dispositivo_empresa/object_detail.html'
    fields = ['id_user', 'nombre', 'apellidos', 'dispositivo', 'activo']

    page = {
        'title': 'Dispositivo/Empleados',
        'subtitle': 'detalles'
    }

    def get_context_data(self, **kwargs):
        context = super(EmpresaDispositivoDetail, self).get_context_data(**kwargs)

        context['dispositivo_empleado'] = EmpleadoClienteDispositivo.objects.select_related('dispositivo', 'empleado')
        context['marcas'] = Marca.objects.filter(dispositivo=self.kwargs['pk'])

        context['page'] = self.page

        return context


class EmpresaAsociarDispositivoCreate(GroupRequiredMixin, SuccessMessageMixin, CreateView):
    # required
    group_required = u"Empresa"

    model = EmpleadoClienteDispositivo

    template_name = 'asistencia_app/empleadoscliente/dispositivo_asociar_empleado_form.html'
    # success_url = reverse_lazy('empleadoscliente_list')
    # success_message = "Empleado registrado satisfactoriamente"
    #fields = ['empleado', 'dispositivo', 'id_user']
    fields = ['empleado', 'dispositivo','id_user']

    page = {
        'title': 'Empleados en dispositivo',
        'subtitle': 'agregar'
    }

    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        #self.object.user = self.request.user

        response_dict = {}

        try:
            self.object.save()
            messages.add_message(
                self.request, messages.SUCCESS,
                'El empleado se asoció correctamente'
            )
            return redirect(self.get_success_url())

        except IntegrityError as e:
            response_dict.update({'error': e})
            messages.add_message(
                self.request, messages.WARNING, 'Error, usuario ya fue asociado')
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, **kwargs):

        return reverse('empresa_empleados_dispositivos')

    def get_context_data(self, **kwargs):
        context = super(EmpresaAsociarDispositivoCreate, self).get_context_data(**kwargs)

        context['form'].fields['dispositivo'].queryset = Dispositivo.objects.filter()
        context['page'] = self.page

        return context


class EmpresaDispositivoDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    # required
    group_required = u"Cliente"

    model = EmpleadoClienteDispositivo

    template_name = 'registros_app/empleadoscliente/empleado_asociar_confirm_delete.html'

    page = {
        'title': 'Empresa',
        'subtitle': 'eliminar de dispositivo'
    }

    def get_success_url(self, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'Se ha eliminado empleado del dispositivo')
        return reverse("empresa_dispositivo_detail", kwargs={"pk": self.kwargs['user_id']})

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EmpresaDispositivoDelete, self).delete(request, *args, **kwargs)

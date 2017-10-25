# -*- coding: utf-8 -*-
from json import dumps

import operator
from django.http import request
from braces.views import GroupRequiredMixin
from django import http
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.shortcuts import HttpResponse
from django.views.generic import View, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from functools import reduce
from pure_pagination.mixins import PaginationMixin
from rest_framework import generics

from intranet_sm.asistencia_app.forms import ExportForm
from intranet_sm.asistencia_app.models import Empleado
from intranet_sm.asistencia_app.models import Marca, EmpleadoClienteDispositivo, Dispositivo
from intranet_sm.asistencia_app.resource import MarcaResource
from intranet_sm.asistencia_app.serializers import MarcaSerializer


class MarcaMixin(object):
    model = Marca


class MarcaList(GroupRequiredMixin, MarcaMixin, PaginationMixin, ListView):
    # required
    group_required = u"Administrador"
    raise_exception = True

    template_name = 'asistencia_app/marcas/object_list.html'
    paginate_by = 50

    page = {
        'title': 'Marcas',
        'subtitle': 'listado'
    }

    def get_context_data(self, **kwargs):
        context = super(MarcaList, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class MarcaEmpleadoList(GroupRequiredMixin, MarcaMixin, PaginationMixin, ListView):
    # required
    group_required = u"Empleados"
    raise_exception = True

    template_name = 'asistencia_app/marcas/empleado/object_list.html'
    paginate_by = 50

    page = {
        'title': 'Marcas',
        'subtitle': 'listado por empleados'
    }

    def get_context_data(self, **kwargs):
        context = super(MarcaEmpleadoList, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    def get_queryset(self):

        dis = EmpleadoClienteDispositivo.objects.filter(
            empleado_id=self.request.user.id)

        if not dis:
            return dis

        empleado_list = []

        for di in dis:
            empleado_list.append(Q(id_user=di.id_user))

        marcas = Marca.objects.filter(
            reduce(operator.or_, empleado_list)).order_by('-start')

        return marcas


class MarcaEmpleadoEmpresaList(GroupRequiredMixin, MarcaMixin, PaginationMixin, ListView):
    # required
    group_required = u"Empresa"
    raise_exception = True

    template_name = 'asistencia_app/marcas/empresa/object_list.html'
    paginate_by = 50

    page = {
        'title': 'Marcas',
        'subtitle': 'listado'
    }

    def get_context_data(self, **kwargs):
        context = super(MarcaEmpleadoEmpresaList, self).get_context_data(**kwargs)
        context['page'] = self.page

        return context

    def get_queryset(self):
        dis = Dispositivo.objects.filter()

        dipositivo_list = []

        for di in dis:
            dipositivo_list.append(Q(dispositivo_id=di.pk))

        marcas = Marca.objects.filter(
            reduce(operator.or_, dipositivo_list)).order_by('-fecha')

        return marcas


class MarcaEmpleadoIndEmpresaList(GroupRequiredMixin, MarcaMixin, PaginationMixin, ListView):
    # required
    group_required = u"Empresa"
    raise_exception = True

    template_name = 'asistencia_app/marcas/empresa/object_list_ind.html'
    paginate_by = 50

    page = {
        'title': 'Marcas',
        'subtitle': 'listado'
    }

    def get_context_data(self, **kwargs):
        context = super(MarcaEmpleadoIndEmpresaList, self).get_context_data(**kwargs)
        context['page'] = self.page

        context['empleado'] = Empleado.objects.get(pk=self.request.GET.get('empleado_id'))

        return context

    def get_queryset(self):

        dis = EmpleadoClienteDispositivo.objects.filter(
            empleado_id=self.request.GET.get('empleado_id'))

        marca_list = []

        for di in dis:

            marcas_f = Marca.objects.filter(
                dispositivo_id=di.dispositivo_id, id_user=di.id_user
            ).order_by('-fecha')

            for m in marcas_f:
                marca_list.append(m.id)

        return Marca.objects.filter(
            id__in=marca_list
        ).order_by('-fecha')


class MarcaDetail(MarcaMixin, DetailView):
    pass


class MarcasCalendar(GroupRequiredMixin, TemplateView):
    # required
    group_required = u"Administrador"
    raise_exception = True

    template_name = "asistencia_app/empleadoscliente/calendar.html"

    page = {
        'title': 'Marcas',
        'subtitle': 'calendario'
    }

    def get_context_data(self, **kwargs):
        context = super(MarcasCalendar, self).get_context_data(**kwargs)

        context['page'] = self.page

        try:
            empleado = Empleado.objects.get(pk=self.kwargs['empleado_id'])
        except Empleado.DoesNotExist:
            empleado = None

        if empleado:
            context['empleado'] = empleado

        try:
            empleadoClienteDispositivo = EmpleadoClienteDispositivo.objects.filter(
                empleado_id = self.kwargs['empleado_id'])
        except EmpleadoClienteDispositivo.DoesNotExist:
            empleadoClienteDispositivo = None

        if empleadoClienteDispositivo:
            context['empleadoClienteDispositivo'] = empleadoClienteDispositivo

        return context


class MarcasCalendarEmpleado(GroupRequiredMixin, TemplateView):
    # required
    group_required = u"Empleados"
    raise_exception = True

    template_name = "asistencia_app/empleadoscliente/calendar_empleado.html"

    page = {
        'title': 'Marcas',
        'subtitle': 'calendario'
    }

    def get_context_data(self, **kwargs):
        context = super(MarcasCalendarEmpleado, self).get_context_data(**kwargs)

        context['page'] = self.page

        try:
            empleado = Empleado.objects.get(pk=self.request.user.id)
        except Empleado.DoesNotExist:
            empleado = None

        if empleado:
            context['empleado'] = empleado

        try:
            empleadoClienteDispositivo = EmpleadoClienteDispositivo.objects.filter(
                empleado_id=self.request.user.id)
        except EmpleadoClienteDispositivo.DoesNotExist:
            empleadoClienteDispositivo = None

        if empleadoClienteDispositivo:
            context['empleadoClienteDispositivo'] = empleadoClienteDispositivo

        return context


class MarcasCalJsonView(View):
    def get(self, request, *args, **kwargs):
        desde = self.request.GET.get('start')
        hasta = self.request.GET.get('end')

        dis = EmpleadoClienteDispositivo.objects.filter(
            empleado_id=self.kwargs['empleado_id'])

        print(dis, self.kwargs['empleado_id'])

        marca_list = []

        for di in dis:
            marcas_f = Marca.objects.filter(
                dispositivo_id=di.dispositivo_id, id_user=di.id_user,
                start__range=[desde, hasta]
            ).order_by('-title')

            for mm in marcas_f:

                fecha = mm.start
                fe = fecha.strftime("%Y-%m-%dT%H:%M:%S")
                # ho = fecha.strftime("%H:%M:%S")
                #dd = {'id': mm.id, 'start': fe, 'title': mm.title, 'tipo': 1}
                dd = {'id': mm.id, 'start': fe, 'title': mm.title}
                marca_list.append(dd)

        response = marca_list

        data = dumps(list(response), cls=DjangoJSONEncoder)

        return http.HttpResponse(data)


class MarcaModalExportView(FormView):
    template_name = 'asistencia_app/marcas/marcas_export.html'
    form_class = ExportForm
    success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        d = self.request.POST['desde']
        h = self.request.POST['hasta']
        q = Marca.objects.filter(fecha__gte=d, fecha__lte=h)
        dataset = MarcaResource().export(q)
        dataset.xls
        response = HttpResponse(dataset.xls, content_type="xls")
        response['Content-Disposition'] = 'attachment; filename=marcasExport.xls'
        return response

    def form_valid(self, form, ):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()

        return super(MarcaModalExportView, self).form_valid(form)


class MarcaEmpresaModalExportView(FormView):
    template_name = 'asistencia_app/marcas/empresa/marcas_export.html'
    form_class = ExportForm
    success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        d = self.request.POST['desde']
        h = self.request.POST['hasta']

        dis = Dispositivo.objects.filter(
            empresa_id=self.kwargs['empresa_id'])

        dipositivo_list = []

        for di in dis:
            dipositivo_list.append(Q(dispositivo_id=di.pk))

        q = Marca.objects.filter(
            reduce(operator.or_, dipositivo_list),
            fecha__gte=d, fecha__lte=h).order_by('-fecha')

        dataset = MarcaResource().export(q)
        dataset.xls
        response = HttpResponse(dataset.xls, content_type="xls")
        response['Content-Disposition'] = 'attachment; filename=marcasExport.xls'
        return response

    def form_valid(self, form, ):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()

        return super(MarcaEmpresaModalExportView, self).form_valid(form)


class MarcaDispositivoModalExportView(FormView):
    template_name = 'asistencia_app/marcas/marcas_export.html'
    form_class = ExportForm
    success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        d = self.request.POST['desde']
        h = self.request.POST['hasta']
        q = Marca.objects.filter(fecha__gte=d, fecha__lte=h, dispositivo_id=self.kwargs['pk'])
        dataset = MarcaResource().export(q)
        dataset.xls
        response = HttpResponse(dataset.xls, content_type="xls")
        response['Content-Disposition'] = 'attachment; filename=marcasExport.xls'
        return response

    def form_valid(self, form, ):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()

        return super(MarcaDispositivoModalExportView, self).form_valid(form)


class MarcaEmpleadoModalExportView(FormView):
    template_name = 'asistencia_app/marcas/marcas_empleado_export.html'
    form_class = ExportForm
    success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        d = self.request.POST['desde']
        h = self.request.POST['hasta']
        '''
        empDipositivo = EmpleadoClienteDispositivo.objects.filter(empleado_id=self.kwargs['pk'])

        disList = []

        for ed in empDipositivo:
            disList.append(Q(id_user=ed.id_user))
        print disList
        q = Marca.objects.filter(
            reduce(operator.or_, disList)
        ).filter(fecha__gte=d, fecha__lte=h,)
        print q
        # q = Marca.objects.filter(fecha__gte=d, fecha__lte=h, id_user=1)
        '''
        q = Marca.objects.filter(fecha__gte=d, fecha__lte=h, dispositivo_id=self.kwargs['d'], id_user=self.kwargs['u'])
        dataset = MarcaResource().export(q)
        dataset.xls
        response = HttpResponse(dataset.xls, content_type="xls")
        response['Content-Disposition'] = 'attachment; filename=marcasEmpleadoExport.xls'
        return response

    def get_context_data(self, **kwargs):
        context = super(MarcaEmpleadoModalExportView, self).get_context_data(**kwargs)
        context.update({
            'id_user': self.kwargs['u'], 'dispositivo_id': self.kwargs['d'],
        })
        return context

    def form_valid(self, form, ):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()

        return super(MarcaEmpleadoModalExportView, self).form_valid(form)


class MarcaEmpleadoIndModalExportView(FormView):
    template_name = 'asistencia_app/marcas/marcas_empleado_export_ind.html'
    form_class = ExportForm
    success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        d = self.request.POST['desde']
        h = self.request.POST['hasta']

        dis = EmpleadoClienteDispositivo.objects.filter(
            empleado_id=self.kwargs['empleado_id']
        )

        print
        dis, 'Dispositivo, ', self.kwargs['empleado_id']

        marca_list = []

        for di in dis:

            marcas_f = Marca.objects.filter(
                dispositivo_id=di.dispositivo_id, id_user=di.id_user
            )

            for m in marcas_f:
                marca_list.append(m.id)
                print
                m

        q = Marca.objects.filter(
            id__in=marca_list,
            fecha__gte=d, fecha__lte=h,
        )

        dataset = MarcaResource().export(q)
        dataset.xls
        response = HttpResponse(dataset.xls, content_type="xls")
        response['Content-Disposition'] = 'attachment; filename=marcasEmpleadoIndExport.xls'
        return response

    def get_context_data(self, **kwargs):
        context = super(MarcaEmpleadoIndModalExportView, self).get_context_data(**kwargs)
        context.update({
            'empleado_id': self.kwargs['empleado_id'],
        })

        context['empleado'] = Empleado.objects.get(pk=self.kwargs['empleado_id'])

        return context

    def form_valid(self, form, ):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()

        return super(MarcaEmpleadoIndModalExportView, self).form_valid(form)


class MarcaApiList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        empleado_id = self.kwargs['empleado_id']
        return Marca.objects.filter(empleado_id=empleado_id)



class MarcaApiDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

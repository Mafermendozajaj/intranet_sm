# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from braces.views import GroupRequiredMixin
from django.views.generic.list import ListView
from pure_pagination.mixins import PaginationMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView
#from intranet.users.models import EmpresaUser

from intranet_sm.asistencia_app.models import EmpleadoClienteDispositivo


class EmpleadoClienteDispositivoList(GroupRequiredMixin,
                                     PaginationMixin, ListView):

    # required
    group_required = u"Empresa"

    model = EmpleadoClienteDispositivo

    template_name = 'asistencia_app/empleado_dispositivo/object_list.html'

    page = {
        'title': 'Empleado',
        'subtitle': 'en dispositivos'
    }

    def get_queryset(self):
        return EmpleadoClienteDispositivo.objects.filter().order_by('dispositivo', 'id_user')

    def get_context_data(self, **kwargs):
        context = super(EmpleadoClienteDispositivoList, self).get_context_data(**kwargs)

        context['page'] = self.page
        return context


class EmpleadoClienteDispositivoDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):

    # required
    group_required = u"Empresa"

    model = EmpleadoClienteDispositivo
    success_url = reverse_lazy('empresa_empleados_dispositivos')
    success_message = "Se ha eliminado el empleado del dispositivo"

    template_name = 'registros_app/empleado_dispositivo/empleado_dispositivo_confirm_delete.html'

    page = {
        'title': 'Empleados',
        'subtitle': 'eliminar de dispositivo'
    }

    '''
    def get_success_url(self, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'Se ha eliminado empleado del dispositivo')


    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EmpleadoClienteDispositivoDelete, self).delete(request, *args, **kwargs)
        #return reverse("empleadoscliente_detail", kwargs={"pk": self.kwargs['pk']})
   '''

    def get_context_data(self, **kwargs):
        context = super(EmpleadoClienteDispositivoDelete, self).get_context_data(**kwargs)
        context['page'] = self.page


        return context

'''
class EmpresaDispositivoList(GroupRequiredMixin, PaginationMixin, ListView):

    # required
    group_required = u"Empresa"

    model = Dispositivo

    template_name = 'registros_app/empleadoscliente/object_list.html'

    page = {
        'title': 'Empleado',
        'subtitle': 'en dispositivos'
    }

    def get_queryset(self):
        return Dispositivo.objects.filter(
            empresa=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(EmpresaDispositivoList, self).get_context_data(**kwargs)

        context['page'] = self.page
        return context


class EmpleadoClienteDetail(GroupRequiredMixin, EmpleadoClienteMixin, DetailView):

    # required
    group_required = u"Cliente"

    template_name = 'registros_app/empleadoscliente/object_detail.html'
    fields = ['id_user', 'nombre', 'apellidos', 'dispositivo', 'activo']

    page = {
        'title': 'Empleados',
        'subtitle': 'detalles'
    }

    def get_context_data(self, **kwargs):
        context = super(EmpleadoClienteDetail, self).get_context_data(**kwargs)
        dis = EmpleadoClienteDispositivo.objects.filter(
              empleado_id=self.kwargs['pk'])

        empleado_list = []

        d = '<ul>'
        for di in dis:
            empleado_list.append(Q(id_user=di.id_user))
            d += '<li>' + di.dispositivo_id + '</li>'
        d += '</ul>'

        context['d'] = d

        context['dispositivo_empleado'] = dis

        if empleado_list:
            context['marcas'] = Marca.objects.filter(reduce(operator.or_, empleado_list))

        context['page'] = self.page

        return context


class EmpleadoCreate(GroupRequiredMixin, EmpleadoClienteMixin, SuccessMessageMixin, CreateView):

    # required
    group_required = u"Cliente"

    template_name = 'registros_app/empleadoscliente/object_form.html'
    success_url = reverse_lazy('empleadoscliente_list')
    success_message = "Empleado registrado satisfactoriamente"
    fields = ['nombre', 'apellidos', 'activo']

    page = {
        'title': 'Empleados cliente',
        'subtitle': 'agregar'
    }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        messages.add_message(self.request, messages.SUCCESS, 'La nota se guardó satifactoriamente')
        return super(EmpleadoCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EmpleadoCreate, self).get_context_data(**kwargs)
        # context['form'].fields['dispositivo'].queryset = Dispositivo.objects.filter(
        #    user_id=self.request.user)
        context['page'] = self.page
        return context


class EmpleadoUpdate(GroupRequiredMixin, EmpleadoClienteMixin, SuccessMessageMixin, UpdateView):

    # required
    group_required = u"Cliente"

    template_name = 'registros_app/empleadoscliente/object_form.html'
    success_url = reverse_lazy('empleadoscliente_list')
    success_message = "Empleado registrado satisfactoriamente"
    fields = ['nombre', 'apellidos', 'activo']

    page = {
        'title': 'Empleados cliente',
        'subtitle': 'actualizar'
    }

    def get_context_data(self, **kwargs):
        context = super(EmpleadoUpdate, self).get_context_data(**kwargs)
        #context['form'].fields['dispositivo'].queryset = Dispositivo.objects.filter(
        #    user_id=self.request.user)
        context['page'] = self.page
        return context


class EmpleadoDelete(GroupRequiredMixin, EmpleadoClienteMixin, SuccessMessageMixin, DeleteView):

    # required
    group_required = u"Cliente"

    template_name = 'registros_app/empleadoscliente/object_confirm_delete.html'
    success_message = "Empleado eliminado satisfactoriamente"
    success_url = reverse_lazy('empleadoscliente_list')

    page = {
        'title': 'Empleados',
        'subtitle': 'eliminación'
    }

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EmpleadoDelete, self).delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDelete, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context




class EmpleadoAsociarCreate(GroupRequiredMixin, SuccessMessageMixin, CreateView):

    # required
    group_required = u"Cliente"

    model = EmpleadoClienteDispositivo

    template_name = 'registros_app/empleadoscliente/dispositivo_asociar_empleado_form.html'
    # success_url = reverse_lazy('empleadoscliente_list')
    # success_message = "Empleado registrado satisfactoriamente"
    fields = ['dispositivo', 'id_user']

    page = {
        'title': 'Empleados cliente dispositivo',
        'subtitle': 'agregar'
    }

    def form_valid(self, form, **kwargs):
        self.object = form.save(commit=False)
        self.object.empleado_id = self.kwargs['pk']
        self.object.user = self.request.user

        response_dict = {}

        try:
            self.object.save()
            messages.add_message(
                self.request, messages.SUCCESS, 'El empleado se asoció correctamente')
            # return super(EmpleadoAsociarCreate, self).form_valid(form)
            return redirect(self.get_success_url())

        except IntegrityError, e:
            response_dict.update({'error': e})
            messages.add_message(
                self.request, messages.WARNING, 'Error, usuario ya fue asociado')
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, **kwargs):

        return reverse('empleadoscliente_detail', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super(EmpleadoAsociarCreate, self).get_context_data(**kwargs)
        context['form'].fields['dispositivo'].queryset = Dispositivo.objects.filter(
            user_id=self.request.user)
        context['page'] = self.page
        return context


class EmpleadoAsociarDelete2(DeleteView):
    model = EmpleadoClienteDispositivo
    success_url = reverse_lazy('empleadoscliente_list')
    template_name = 'registros_app/empleadoscliente/empleado_asociar_confirm_delete.html'




class MarcaModalExportView(FormView):
    template_name = 'registros_app/marcas/marcas_export.html'
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


class MarcaEmpleadoModalExportView(FormView):
    template_name = 'registros_app/marcas/marcas_empleado_export.html'
    form_class = ExportForm
    success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        d = self.request.POST['desde']
        h = self.request.POST['hasta']
        empDipositivo = EmpleadoClienteDispositivo.objects.filter(empleado_id=self.kwargs['pk'])

        #disList = [Q(id_user=114)]
        disList = []

        for ed in empDipositivo:
            disList.append(Q(id_user=ed.id_user))
        print disList
        q = Marca.objects.filter(
            reduce(operator.or_, disList)
        ).filter(fecha__gte=d, fecha__lte=h,)
        print q
        # q = Marca.objects.filter(fecha__gte=d, fecha__lte=h, id_user=1)
        dataset = MarcaResource().export(q)
        dataset.xls
        response = HttpResponse(dataset.xls, content_type="xls")
        response['Content-Disposition'] = 'attachment; filename=marcasEmpleadoExport.xls'
        return response


    def get_context_data(self, **kwargs):
        context = super(MarcaEmpleadoModalExportView, self).get_context_data(**kwargs)
        context.update({
            'id_user': self.kwargs['pk'],
        })
        return context


    def form_valid(self, form, ):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()

        return super(MarcaEmpleadoModalExportView, self).form_valid(form)
'''

from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin

from intranet_sm.solicitudes_app.models import Constancia, Empleado

from reportlab.pdfgen import canvas
from django.http import HttpResponse


class ConstanciaListView(LoginRequiredMixin, PaginationMixin, ListView):

    model = Constancia
    template_name = 'solicitudes_app/constancias/constancia_list.html'
    context_object_name = 'constancia_list'
    paginate_by = 50

    page = {
        'title': 'Constancia',
        'subtitle': 'constancias'
    }

    def get_context_data(self, **kwargs):
        context = super(ConstanciaListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class ConstanciaCreateView(LoginRequiredMixin, CreateView):

    fields = [
        'tipo_constancia'
    ]

    model = Constancia
    template_name = 'solicitudes_app/constancias/constancia_form.html'

    page = {
        'title': 'Constancia',
        'subtitle': 'edicion de constancias'
    }

    def get_context_data(self, **kwargs):
        context = super(ConstanciaCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('solicitudes:constancia_list')

    def form_valid(self, form):
        empleado = Empleado.objects.get(pk=self.request.user.id)
        self.object = form.save(commit=False)
        self.object.empleado = empleado
        if self.object.tipo_constancia == 'SS':
            self.object.estado_constancia = "C"
        else:
            self.object.estado_constancia = "N"
        self.object.save()
        return super(ConstanciaCreateView, self).form_valid(form)


class ConstanciaDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'empleado','fecha_solicitud','fecha_aprobacion','sueldo','tipo_constancia','estado_constancia',
    ]

    model = Constancia
    template_name = 'solicitudes_app/constancias/constancia_detail.html'

    page = {
        'title': 'Constancia',
        'subtitle': 'edicion de constancias'
    }

    def get_context_data(self, **kwargs):
        context = super(ConstanciaDetailView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class ConstanciaUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        'sueldo'
    ]

    model = Constancia
    template_name = 'solicitudes_app/constancias/constancia_form.html'

    page = {
        'title': 'Constancia',
        'subtitle': 'edicion de constancias'
    }

    def get_context_data(self, **kwargs):
        context = super(ConstanciaUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


    def form_valid(self, form):
        empleado = Empleado.objects.get(pk=self.request.user.id)
        self.object = form.save(commit=False)
        self.object.empleado = empleado
        if self.object.sueldo == '0':
            self.object.estado_constancia = "N"
        else:
            self.object.estado_constancia = "C"
        self.object.save()
        return super(ConstanciaUpdateView, self).form_valid(form)

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('solicitudes:constancia_list')


class ConstanciaDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'empleado','fecha_solicitud','fecha_aprobacion','sueldo','tipo_constancia','estado_constancia',
    ]

    model = Constancia
    template_name = 'solicitudes_app/constancias/constancia_confirm_delete.html'

    page = {
        'title': 'Constancia',
        'subtitle': 'edicion de constancias'
    }

    def get_context_data(self, **kwargs):
        context = super(ConstanciaDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('solicitudes:constancia_list')


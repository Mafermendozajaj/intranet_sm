from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin

from intranet_sm.users.models import Reporte


class ReporteListView(LoginRequiredMixin, PaginationMixin, ListView):

    model = Reporte
    template_name = 'administrator_app/reportes/reporte_list.html'
    context_object_name = 'reporte_list'
    paginate_by = 50

    page = {
        'title': 'Administrador',
        'subtitle': 'reportes'
    }

    def get_context_data(self, **kwargs):
        context = super(ReporteListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class ReporteCreateView(LoginRequiredMixin, CreateView):

    fields = [
        'reporte',
    ]

    model = Reporte
    template_name = 'administrator_app/reportes/reporte_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'edicion de reportes'
    }

    def get_context_data(self, **kwargs):
        context = super(ReporteCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:reporte_list')


class ReporteDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'reporte',
    ]

    model = Reporte
    template_name = 'administrator_app/reportes/reporte_detail.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'edicion de reportes'
    }

    def get_context_data(self, **kwargs):
        context = super(ReporteDetailView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class ReporteUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        'reporte',
    ]

    model = Reporte
    template_name = 'administrator_app/reportes/reporte_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'edicion de reportes'
    }

    def get_context_data(self, **kwargs):
        context = super(ReporteUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:reporte_list')


class ReporteDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'reporte',
    ]

    model = Reporte
    template_name = 'administrator_app/reportes/reporte_confirm_delete.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'edicion de reportes'
    }

    def get_context_data(self, **kwargs):
        context = super(ReporteDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:reporte_list')


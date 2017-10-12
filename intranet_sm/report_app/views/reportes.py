from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin

from intranet_sm.report_app.models import Reporte


class ReporteListView(LoginRequiredMixin, PaginationMixin, ListView):

    model = Reporte
    template_name = 'report_app/reportes/reporte_list.html'
    context_object_name = 'reporte_list'
    paginate_by = 50

    page = {
        'title': 'Reporte',
        'subtitle': 'reportes'
    }

    def get_context_data(self, **kwargs):
        context = super(ReporteListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class ReporteCreateView(LoginRequiredMixin, CreateView):

    fields = [
        'asistente','observador','proyecto','tipo_reporte','telescopio',
        'fecha_obs','datos','observadores','horas_trabajadas','hp_clima',
        'hp_instrumentos','hp_software','comentarios','vacio_camara',
        'vacio_ls','vacio_li','enviado'
    ]

    model = Reporte
    template_name = 'report_app/reportes/reporte_form.html'

    page = {
        'title': 'Reporte',
        'subtitle': 'edicion de reportes'
    }

    def get_context_data(self, **kwargs):
        context = super(ReporteCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('report:reporte_list')


class ReporteDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'reporte',
    ]

    model = Reporte
    template_name = 'report_app/reportes/reporte_detail.html'

    page = {
        'title': 'Reporte',
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
    template_name = 'report_app/reportes/reporte_form.html'

    page = {
        'title': 'Reporte',
        'subtitle': 'edicion de reportes'
    }

    def get_context_data(self, **kwargs):
        context = super(ReporteUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('report:reporte_list')


class ReporteDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'reporte',
    ]

    model = Reporte
    template_name = 'report_app/reportes/reporte_confirm_delete.html'

    page = {
        'title': 'Reporte',
        'subtitle': 'edicion de reportes'
    }

    def get_context_data(self, **kwargs):
        context = super(ReporteDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('report:reporte_list')


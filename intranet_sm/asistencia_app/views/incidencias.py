from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin

from intranet_sm.asistencia_app.models import Incidencia


class IncidenciaListView(LoginRequiredMixin, PaginationMixin, ListView):

    model = Incidencia
    template_name = 'asistencia_app/incidencias/incidencia_list.html'
    context_object_name = 'incidencia'
    paginate_by = 50

    page = {
        'title': 'Incidencia',
        'subtitle': 'incidencias'
    }

    def get_context_data(self, **kwargs):
        context = super(IncidenciaListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class IncidenciaCreateView(LoginRequiredMixin, CreateView):

    fields = [
        'title',
    ]

    model = Incidencia
    template_name = 'asistencia_app/incidencias/incidencia_form.html'

    page = {
        'title': 'Incidencia',
        'subtitle': 'edicion de incidencias'
    }

    def get_context_data(self, **kwargs):
        context = super(IncidenciaCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('asistencias:incidencia_list')


class IncidenciaDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'title','start','end'
    ]

    model = Incidencia
    template_name = 'asistencia_app/incidencias/incidencia_detail.html'

    page = {
        'title': 'Incidencia',
        'subtitle': 'edicion de incidencias'
    }


class IncidenciaUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        'title','start','end'
    ]

    model = Incidencia
    template_name = 'asistencia_app/incidencias/incidencia_form.html'

    page = {
        'title': 'Incidencia',
        'subtitle': 'edicion de incidencias'
    }

    def get_context_data(self, **kwargs):
        context = super(IncidenciaUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('asistencias:incidencia_list')


class IncidenciaDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'title','start','end'
    ]

    model = Incidencia
    template_name = 'asistencia_app/incidencias/incidencia_confirm_delete.html'

    page = {
        'title': 'Incidencia',
        'subtitle': 'edicion de incidencias'
    }

    def get_context_data(self, **kwargs):
        context = super(IncidenciaDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('asistencias:incidencia_list')


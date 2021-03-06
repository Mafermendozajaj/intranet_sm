from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin

from intranet_sm.report_app.models import Proyecto


class ProyectoListView(LoginRequiredMixin, PaginationMixin, ListView):

    model = Proyecto
    template_name = 'report_app/proyectos/proyecto_list.html'
    context_object_name = 'proyecto_list'
    paginate_by = 50

    page = {
        'title': 'Proyecto',
        'subtitle': 'proyectos'
    }

    def get_context_data(self, **kwargs):
        context = super(ProyectoListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class ProyectoCreateView(LoginRequiredMixin, CreateView):

    fields = [
        'proyecto','cod_proyecto'
    ]

    model = Proyecto
    template_name = 'report_app/proyectos/proyecto_form.html'

    page = {
        'title': 'Proyecto',
        'subtitle': 'edicion de proyectos'
    }

    def get_context_data(self, **kwargs):
        context = super(ProyectoCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('report:proyecto_list')


class ProyectoDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'proyecto','cod_proyecto'
    ]

    model = Proyecto
    template_name = 'report_app/proyectos/proyecto_detail.html'

    page = {
        'title': 'Proyecto',
        'subtitle': 'edicion de proyectos'
    }

    def get_context_data(self, **kwargs):
        context = super(ProyectoDetailView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class ProyectoUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        'proyecto','cod_proyecto'
    ]

    model = Proyecto
    template_name = 'report_app/proyectos/proyecto_form.html'

    page = {
        'title': 'Proyecto',
        'subtitle': 'edicion de proyectos'
    }

    def get_context_data(self, **kwargs):
        context = super(ProyectoUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('report:proyecto_list')


class ProyectoDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'proyecto','cod_proyecto'
    ]

    model = Proyecto
    template_name = 'report_app/proyectos/proyecto_confirm_delete.html'

    page = {
        'title': 'Proyecto',
        'subtitle': 'edicion de proyectos'
    }

    def get_context_data(self, **kwargs):
        context = super(ProyectoDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('report:proyecto_list')


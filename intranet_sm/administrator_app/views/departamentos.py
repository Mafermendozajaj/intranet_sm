from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin

from intranet_sm.users.models import Departamento


class DepartamentoListView(LoginRequiredMixin, PaginationMixin, ListView):

    model = Departamento
    template_name = 'administrator_app/departamentos/departamento_list.html'
    context_object_name = 'departamento_list'
    paginate_by = 50

    page = {
        'title': 'Administrador',
        'subtitle': 'departamentos'
    }

    def get_context_data(self, **kwargs):
        context = super(DepartamentoListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class DepartamentoCreateView(LoginRequiredMixin, CreateView):

    fields = [
        'departamento',
    ]

    model = Departamento
    template_name = 'administrator_app/departamentos/departamento_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'edicion de departamentos'
    }

    def get_context_data(self, **kwargs):
        context = super(DepartamentoCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:departamento_list')


class DepartamentoDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'departamento',
    ]

    model = Departamento
    template_name = 'administrator_app/departamentos/departamento_detail.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'edicion de departamentos'
    }

    def get_context_data(self, **kwargs):
        context = super(DepartamentoDetailView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class DepartamentoUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        'departamento',
    ]

    model = Departamento
    template_name = 'administrator_app/departamentos/departamento_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'edicion de departamentos'
    }

    def get_context_data(self, **kwargs):
        context = super(DepartamentoUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:departamento_list')


class DepartamentoDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'departamento',
    ]

    model = Departamento
    template_name = 'administrator_app/departamentos/departamento_confirm_delete.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'edicion de departamentos'
    }

    def get_context_data(self, **kwargs):
        context = super(DepartamentoDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:departamento_list')


from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin

from intranet_sm.users.models import Telescopio


class TelescopioListView(LoginRequiredMixin, PaginationMixin, ListView):

    model = Telescopio
    template_name = 'administrator_app/telescopioss/telescopio_list.html'
    context_object_name = 'telescopio_list'
    paginate_by = 50

    page = {
        'title': 'Administrador',
        'subtitle': 'telescopioss'
    }

    def get_context_data(self, **kwargs):
        context = super(TelescopioListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class TelescopioCreateView(LoginRequiredMixin, CreateView):

    fields = [
        'telescopio',
    ]

    model = Telescopio
    template_name = 'administrator_app/telescopioss/telescopio_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'edicion de telescopioss'
    }

    def get_context_data(self, **kwargs):
        context = super(TelescopioCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:telescopio_list')


class TelescopioDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'telescopio',
    ]

    model = Telescopio
    template_name = 'administrator_app/telescopioss/telescopio_detail.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'edicion de telescopioss'
    }

    def get_context_data(self, **kwargs):
        context = super(TelescopioDetailView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class TelescopioUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        'telescopio',
    ]

    model = Telescopio
    template_name = 'administrator_app/telescopioss/telescopio_form.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'edicion de telescopioss'
    }

    def get_context_data(self, **kwargs):
        context = super(TelescopioUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:telescopio_list')


class TelescopioDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'telescopio',
    ]

    model = Telescopio
    template_name = 'administrator_app/telescopioss/telescopio_confirm_delete.html'

    page = {
        'title': 'Administrador',
        'subtitle': 'edicion de telescopioss'
    }

    def get_context_data(self, **kwargs):
        context = super(TelescopioDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('administrator:telescopio_list')


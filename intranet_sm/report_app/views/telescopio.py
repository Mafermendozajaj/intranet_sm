from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin

from intranet_sm.report_app.models import Telescopio


class TelescopioListView(LoginRequiredMixin, PaginationMixin, ListView):

    model = Telescopio
    template_name = 'report_app/telescopios/telescopio_list.html'
    context_object_name = 'telescopio_list'
    paginate_by = 50

    page = {
        'title': 'Telescopio',
        'subtitle': 'telescopios'
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
    template_name = 'report_app/telescopios/telescopio_form.html'

    page = {
        'title': 'Telescopio',
        'subtitle': 'edicion de telescopios'
    }

    def get_context_data(self, **kwargs):
        context = super(TelescopioCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('report:telescopio_list')


class TelescopioDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'telescopio',
    ]

    model = Telescopio
    template_name = 'report_app/telescopios/telescopio_detail.html'

    page = {
        'title': 'Telescopio',
        'subtitle': 'edicion de telescopios'
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
    template_name = 'report_app/telescopios/telescopio_form.html'

    page = {
        'title': 'Telescopio',
        'subtitle': 'edicion de telescopios'
    }

    def get_context_data(self, **kwargs):
        context = super(TelescopioUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('report:telescopio_list')


class TelescopioDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'telescopio',
    ]

    model = Telescopio
    template_name = 'report_app/telescopios/telescopio_confirm_delete.html'

    page = {
        'title': 'Telescopio',
        'subtitle': 'edicion de telescopios'
    }

    def get_context_data(self, **kwargs):
        context = super(TelescopioDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('report:telescopio_list')


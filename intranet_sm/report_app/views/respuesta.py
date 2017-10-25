from django.core.urlresolvers import reverse
from django.views.generic import (
    DetailView, ListView, RedirectView,
    UpdateView, CreateView, DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin

from intranet_sm.report_app.models import Respuesta, Reporte


class RespuestaListView(LoginRequiredMixin, PaginationMixin, ListView):

    model = Respuesta
    template_name = 'report_app/respuestas/respuesta_list.html'
    context_object_name = 'respuesta_list'
    paginate_by = 50

    page = {
        'title': 'Respuesta',
        'subtitle': 'respuestas'
    }

    def get_context_data(self, **kwargs):
        context = super(RespuestaListView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context


class RespuestaCreateView(LoginRequiredMixin, CreateView):

    fields = [
        'respuesta'
    ]

    model = Respuesta
    template_name = 'report_app/respuestas/respuesta_form.html'

    page = {
        'title': 'Respuesta',
        'subtitle': 'edicion de respuestas'
    }

    def get_context_data(self, **kwargs):
        context = super(RespuestaCreateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        context['reporte'] = Reporte.objects.get(pk=self.kwargs['reporte_id'])
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.reporte_id = self.kwargs['reporte_id']
        self.object.save()
        return super(RespuestaCreateView, self).form_valid(form)

    # send the user back to their own page after a successful update
    def get_success_url(self, **kwargs):
        return reverse('report:reporte_view', kwargs={"pk": self.kwargs['reporte_id']})


class RespuestaDetailView(LoginRequiredMixin, DetailView):

    fields = [
        'respuesta'
    ]

    model = Respuesta
    template_name = 'report_app/respuestas/respuesta_detail.html'

    page = {
        'title': 'Respuesta',
        'subtitle': 'edicion de respuestas'
    }

    def get_context_data(self, **kwargs):
        context = super(RespuestaDetailView, self).get_context_data(**kwargs)
        context['page'] = self.page

        return context


class RespuestaUpdateView(LoginRequiredMixin, UpdateView):

    fields = [
        'respuesta'
    ]

    model = Respuesta
    template_name = 'report_app/respuestas/respuesta_form.html'

    page = {
        'title': 'Respuesta',
        'subtitle': 'edicion de respuestas'
    }

    def get_context_data(self, **kwargs):
        context = super(RespuestaUpdateView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('report:respuesta_list')


class RespuestaDeleteView(LoginRequiredMixin, DeleteView):

    fields = [
        'respuesta'
    ]

    model = Respuesta
    template_name = 'report_app/respuestas/respuesta_confirm_delete.html'

    page = {
        'title': 'Respuesta',
        'subtitle': 'edicion de respuestas'
    }

    def get_context_data(self, **kwargs):
        context = super(RespuestaDeleteView, self).get_context_data(**kwargs)
        context['page'] = self.page
        return context

    # send the user back to their own page after a successful update
    def get_success_url(self, **kwargs):
        return reverse('report:reporte_view', kwargs={"pk": self.kwargs['reporte_id']})
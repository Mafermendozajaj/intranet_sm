# -*- coding: utf-8 -*-
from braces.views import LoginRequiredMixin
from django.views.generic import RedirectView, TemplateView
from django.core.urlresolvers import reverse
from intranet_sm.users.models import User


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)

        return context


class Profile(RedirectView):

    permanent = False
    query_string = True

    def get_redirect_url(self):

        user = User.objects.get(id=self.request.user.id)
        if user.groups.filter(name='VentasCliente').exists():
            return reverse('clientesalmacen_dash_view')
        else:
            return reverse('dashboard')

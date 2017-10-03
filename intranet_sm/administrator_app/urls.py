from django.conf.urls import url

from intranet_sm.administrator_app.views import departamentos

urlpatterns = [
    url(
        regex=r'^departamento/$',
        view=departamentos.DepartamentoListView.as_view(),
        name='departamento_list'
    ),
    url(
        regex=r'^departamento/create/$',
        view=departamentos.DepartamentoCreateView.as_view(),
        name='departamento_create'
    ),

    url(
        regex=r'^departamento/view/(?P<pk>\d+)$',
        view=departamentos.DepartamentoDetailView.as_view(),
        name='departamento_view'
    ),

    url(
        regex=r'^departamento/update/(?P<pk>\d+)$',
        view=departamentos.DepartamentoUpdateView.as_view(),
        name='departamento_update'
    ),

    url(
        regex=r'^departamento/delete/(?P<pk>\d+)$',
        view=departamentos.DepartamentoDeleteView.as_view(),
        name='departamento_delete'
    ),

]

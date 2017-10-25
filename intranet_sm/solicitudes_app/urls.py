from django.conf.urls import url

from intranet_sm.solicitudes_app.views import constancias

urlpatterns = [
    url(
        regex=r'^constancia/$',
        view=constancias.ConstanciaListView.as_view(),
        name='constancia_list'
    ),
    url(
        regex=r'^constancia/create/$',
        view=constancias.ConstanciaCreateView.as_view(),
        name='constancia_create'
    ),

    url(
        regex=r'^constancia/view/(?P<pk>\d+)$',
        view=constancias.ConstanciaDetailView.as_view(),
        name='constancia_view'
    ),

    url(
        regex=r'^constancia/update/(?P<pk>\d+)$',
        view=constancias.ConstanciaUpdateView.as_view(),
        name='constancia_update'
    ),

    url(
        regex=r'^constancia/delete/(?P<pk>\d+)$',
        view=constancias.ConstanciaDeleteView.as_view(),
        name='constancia_delete'
    ),
    
]

from django.conf.urls import url

from intranet_sm.reporte_app.views import reportes

urlpatterns = [
    url(
        regex=r'^reporte/$',
        view=reportes.ReporteListView.as_view(),
        name='reporte_list'
    ),
    url(
        regex=r'^reporte/create/$',
        view=reportes.ReporteCreateView.as_view(),
        name='reporte_create'
    ),

    url(
        regex=r'^reporte/view/(?P<pk>\d+)$',
        view=reportes.ReporteDetailView.as_view(),
        name='reporte_view'
    ),

    url(
        regex=r'^reporte/update/(?P<pk>\d+)$',
        view=reportes.ReporteUpdateView.as_view(),
        name='reporte_update'
    ),

    url(
        regex=r'^reporte/delete/(?P<pk>\d+)$',
        view=reportes.ReporteDeleteView.as_view(),
        name='reporte_delete'
    ),

]
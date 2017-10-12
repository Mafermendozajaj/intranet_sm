from django.conf.urls import url

from intranet_sm.report_app.views import reportes, telescopio, proyectos

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

    
#Telescopio
    url(
        regex=r'^telescopio/$',
        view=telescopio.TelescopioListView.as_view(),
        name='telescopio_list'
    ),
    url(
        regex=r'^telescopio/create/$',
        view=telescopio.TelescopioCreateView.as_view(),
        name='telescopio_create'
    ),

    url(
        regex=r'^telescopio/view/(?P<pk>\d+)$',
        view=telescopio.TelescopioDetailView.as_view(),
        name='telescopio_view'
    ),

    url(
        regex=r'^telescopio/update/(?P<pk>\d+)$',
        view=telescopio.TelescopioUpdateView.as_view(),
        name='telescopio_update'
    ),

    url(
        regex=r'^telescopio/delete/(?P<pk>\d+)$',
        view=telescopio.TelescopioDeleteView.as_view(),
        name='telescopio_delete'
    ),


#Proyecto
    url(
        regex=r'^proyecto/$',
        view=proyectos.ProyectoListView.as_view(),
        name='proyecto_list'
    ),
    url(
        regex=r'^proyecto/create/$',
        view=proyectos.ProyectoCreateView.as_view(),
        name='proyecto_create'
    ),

    url(
        regex=r'^proyecto/view/(?P<pk>\d+)$',
        view=proyectos.ProyectoDetailView.as_view(),
        name='proyecto_view'
    ),

    url(
        regex=r'^proyecto/update/(?P<pk>\d+)$',
        view=proyectos.ProyectoUpdateView.as_view(),
        name='proyecto_update'
    ),

    url(
        regex=r'^proyecto/delete/(?P<pk>\d+)$',
        view=proyectos.ProyectoDeleteView.as_view(),
        name='proyecto_delete'
    ),


]
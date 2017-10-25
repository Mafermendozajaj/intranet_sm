from django.conf.urls import url

from intranet_sm.asistencia_app.views.dispositivos import (
    DispositivoList,
    DispositivoCreate,
    DispositivoUpdate,
    DispositivoDelete,
)
from intranet_sm.asistencia_app.views.empresas import (
    EmpresaDispositivoList,
    EmpresaDispositivoDetail,
    EmpresaAsociarDispositivoCreate,
    EmpresaDispositivoDelete,
)
from intranet_sm.asistencia_app.views.empresas_dispositivos import (
    EmpleadoClienteDispositivoList,
    EmpleadoClienteDispositivoDelete,
)
from intranet_sm.asistencia_app.views.marcas import (
    MarcaList,
    MarcaEmpleadoList,
    MarcaDetail,
    MarcaEmpleadoModalExportView,
    MarcaModalExportView,
    MarcaDispositivoModalExportView,
    MarcaEmpleadoEmpresaList,
    MarcaEmpleadoIndEmpresaList,
    MarcaEmpresaModalExportView,
    MarcasCalendar,
    MarcasCalendarEmpleado,
    MarcasCalJsonView,
    MarcaEmpleadoIndModalExportView,
    MarcaApiList,
    MarcaApiDetail
)
from intranet_sm.asistencia_app.views.notas import (
    NotaListApi,
    NotaDetail
)

from intranet_sm.asistencia_app.views import incidencias

urlpatterns = [

    url(r'^admin/dispositivos$', DispositivoList.as_view(), name='dispositivo_list'),
    url(r'^admin/dispositivos/create$',
        DispositivoCreate.as_view(), name='dispositivo_create'),
    url(r'^admin/dispositivos/update/(?P<pk>\d+)$',
        DispositivoUpdate.as_view(), name='dispositivo_update'),
    url(r'^admin/dispositivos/delete/(?P<pk>\d+)$',
        DispositivoDelete.as_view(), name='dispositivo_delete'),
    url(r'^admin/marcas$', MarcaList.as_view(), name='marcas_list'),

    url(r'^empleados/export/global$', MarcaModalExportView.as_view(),
        name='empleados_export_global'),

    url(r'^marcas/empleado$', MarcaEmpleadoList.as_view(),
        name='marcas_empleado_list'),

    url(r'^marcas/detail$', MarcaDetail.as_view(), name='marcas_detail'),

    url(r'^marcas/dispositivos$', EmpresaDispositivoList.as_view(),
        name='empresa_dispositivos_list'),
    url(r'^marcas/dispositivos/(?P<pk>\d+)$',
        EmpresaDispositivoDetail.as_view(), name='empresa_dispositivo_detail'),
    url(r'^marcas/dispositivos/delete/(?P<pk>\d+)$',
        EmpresaDispositivoDelete.as_view(), name='empresa_dispositivos_delete'),
    url(r'^marcas/emp_list$', MarcaEmpleadoEmpresaList.as_view(),
        name='empresa_marcas_empleados'),
    url(r'^marcas/emp_list/ind/$', MarcaEmpleadoIndEmpresaList.as_view(),
        name='empresa_marcas_empleados_ind'),

    url(r'^marcas/empresa_calendar/(?P<empleado_id>\d+)$',
        MarcasCalendar.as_view(), name='empresa_marcas_calendar'),
    url(r'^marcas/empleado_calendar/$', MarcasCalendarEmpleado.as_view(),
        name='empleado_marcas_calendar'),

    url(r'^marcas/emp_calendar/json/(?P<empleado_id>\d+)/$',
        MarcasCalJsonView.as_view(), name='empresa_marcas_json'),

    url(r'^marcas/emp_calendar/api/notas/(?P<empleado_id>\d+)/$',
        NotaListApi.as_view()),
    url(
        r'^marcas/emp_calendar/api/notas/(?P<empleado_id>\d+)/(?P<pk>[0-9]+)/$', NotaDetail.as_view()),

    url(r'^marcas/emp_calendar/api/marcas/(?P<empleado_id>\d+)/$',
        MarcaApiList.as_view()),
    url(
        r'^marcas/emp_calendar/api/marcas/(?P<empleado_id>\d+)/(?P<pk>[0-9]+)/$', MarcaApiDetail.as_view()),


    url(r'^export/empleado/ind/(?P<empleado_id>\d+)$',
        MarcaEmpleadoIndModalExportView.as_view(), name='empresa_export_empleado_ind'),
    url(r'^export/empleado/(?P<pk>\d+)$',
        MarcaEmpleadoModalExportView.as_view(), name='empresa_export_empleado'),
    url(r'^export/marcas/(?P<empresa_id>\d+)$',
        MarcaEmpresaModalExportView.as_view(), name='empresa_export_marca'),

    url(r'^marcas/dispositivo_empl/$', EmpleadoClienteDispositivoList.as_view(),
        name='empresa_empleados_dispositivos'),

    url(r'^dispositivos/asociar/$', EmpresaAsociarDispositivoCreate.as_view(),
        name='empresa_empleados_dispositivos_add'),
    url(r'^dispositivos/asociar/delete/(?P<pk>\d+)$',
        EmpleadoClienteDispositivoDelete.as_view(), name='empresa_empleados_dispositivos_delete'),

    url(r'^export/dispositivo/(?P<pk>\d+)$',
        MarcaDispositivoModalExportView.as_view(), name='empresa_export_dispositivo'),
    url(r'^export/empleado/(?P<d>\d+)/(?P<u>\d+)$',
        MarcaEmpleadoModalExportView.as_view(), name='empresa_export_empleado'),


#Incidencias
    url(
        regex=r'^incidencia/$',
        view=incidencias.IncidenciaListView.as_view(),
        name='incidencia_list'
    ),
    url(
        regex=r'^incidencia/create/$',
        view=incidencias.IncidenciaCreateView.as_view(),
        name='incidencia_create'
    ),

    url(
        regex=r'^incidencia/view/(?P<pk>\d+)$',
        view=incidencias.IncidenciaDetailView.as_view(),
        name='incidencia_view'
    ),

    url(
        regex=r'^incidencia/update/(?P<pk>\d+)$',
        view=incidencias.IncidenciaUpdateView.as_view(),
        name='incidencia_update'
    ),

    url(
        regex=r'^incidencia/delete/(?P<pk>\d+)$',
        view=incidencias.IncidenciaDeleteView.as_view(),
        name='incidencia_delete'
    ),



]

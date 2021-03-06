from django.conf.urls import patterns, url, include

import views

reports = patterns(
    '',
    url(
        r'^solicitud-examenes-clinicos/(?P<control_id>\d+)/$',
        views.SolicitudExamenesClinicosReportView.as_view(),
        name='solicitud_examenes_clinicos'),
    url(
        r'historia-clinica/(?P<control_id>\d+)/$',
        views.HistoriaClinicaReportView.as_view(),
        name='historia_clinica'),
    url(
        r'historia-clinica/(?P<control_id>\d+)/(?P<accion_id>\d+)/$',
        views.HistoriaClinicaReportView.as_view(),
        name='historia_clinica'),
    url(
        r'plan-parto/(?P<control_id>\d+)/$',
        views.PlanPartoReportView.as_view(),
        name='plan_parto'),
    url(
        r'plan-parto/(?P<control_id>\d+)/(?P<accion_id>\d+)/$',
        views.PlanPartoReportView.as_view(),
        name='plan_parto'),
    url(
        r'tarjeta-seguimiento/(?P<control_id>\d+)/$',
        views.TarjetaSeguimientoReportView.as_view(),
        name='tarjeta_seguimiento'),
    url(
        r'receta-unica-estandarizada/(?P<control_id>\d+)/$',
        views.RecetaUnicaEstandarizadaReportView.as_view(),
        name='receta_unica_estandarizada'),
    url(
        r'receta-unica-flujo-vaginal/(?P<control_id>\d+)/$',
        views.RecetaUnicaFlujoVaginalReportView.as_view(),
        name='receta_unica_flujo_vaginal'),
    url(
        r'receta-unica-prueba-rapida/(?P<control_id>\d+)/$',
        views.RecetaUnicaPruebaRapidaReportView.as_view(),
        name='receta_unica_prueba_rapida'),
    url(
        r'formato-unico-atencion/(?P<control_id>\d+)/$',
        views.FormatoUnicoAtencionReportView.as_view(),
        name='formato_unico_atencion'),
    url(
        r'hoja-referencia/(?P<control_id>\d+)/$',
        views.HojaReferenciaReportView.as_view(),
        name='hoja_referencia'),
    url(
        r'carne-control-prenatal/(?P<control_id>\d+)/$',
        views.CarneControlPrenatalReportView.as_view(),
        name='carne_control_prenatal'),
    url(
        r'^solicitud-examen-citologico/(?P<control_id>\d+)/$',
        views.SolicitudExamenCitologicoReportView.as_view(),
        name='solicitud_examen_citologico'),
    url(
        r'^solicitud-prueba-elisa/(?P<control_id>\d+)/$',
        views.SolicitudPruebaElisaReportView.as_view(),
        name='solicitud_prueba_elisa'),
    url(
        r'^control-prenatal-excel/(?P<control_id>\d+)/$',
        views.ControlPrenatalExcelReportView.as_view(),
        name='control_prenatal_excel'),
    url(
        r'^control-prenatal-excel/(?P<control_id>\d+)/(?P<accion_id>\d+)/$',
        views.ControlPrenatalExcelReportView.as_view(),
        name='control_prenatal_excel')
)

fua = patterns(
    '',
    url(
        r'^009/(?P<control_id>\d+)/$',
        views.Fua009ExcelReportView.as_view(),
        name='009'),
    url(
        r'^011/(?P<control_id>\d+)/$',
        views.Fua011ExcelReportView.as_view(),
        name='011'),
    url(
        r'^013/(?P<control_id>\d+)/$',
        views.Fua013ExcelReportView.as_view(),
        name='013'),
    url(
        r'^024/(?P<control_id>\d+)/$',
        views.Fua024ExcelReportView.as_view(),
        name='024'),
    url(
        r'^071/(?P<control_id>\d+)/$',
        views.Fua071ExcelReportView.as_view(),
        name='071'),
)

urlpatterns = patterns(
    '',
    url(r'^reportes/', include(reports, namespace='reports')),
    url(r'^fua/', include(fua, namespace='fua')),
    url(
        r'^(?P<paciente_id>\d+)/controles/$',
        views.ControlesView.as_view(),
        name='list'),
    url(
        r'^control/(?P<id>\d+)/$',
        views.ControlDetailView.as_view(),
        name='detail'),
    url(
        r'^control/(?P<id>\d+)/editar/$',
        views.ControlUpdateView.as_view(),
        name='edit'),
    url(
        r'^control/(?P<id>\d+)/eiminar/$',
        views.ControlDeleteView.as_view(),
        name='delete'),
    url(
        r'^control/(?P<id>\d+)/sintomas/$',
        views.SintomasDetailView.as_view(),
        name='sintomas_detail'),
    url(
        r'^control/(?P<id>\d+)/sintomas/edit/$',
        views.SintomasView.as_view(),
        name='sintomas'),
    url(
        r'^control/(?P<id>\d+)/diagnostico/$',
        views.DiagnosticoDetailView.as_view(),
        name='diagnostico_detail'),
    url(
        r'^control/(?P<id>\d+)/diagnostico/editar/$',
        views.DiagnosticoView.as_view(),
        name='diagnostico'),
    url(
        r'^control/(?P<id>\d+)/examen-fisico/$',
        views.ExamenFisicoDetailView.as_view(),
        name='examen_fisico_detail'),
    url(
        r'^control/(?P<id>\d+)/examen-fisico/editar/$',
        views.ExamenFisicoView.as_view(),
        name='examen_fisico'),
    url(
        r'^control/(?P<id>\d+)/laboratorio/$',
        views.LaboratorioDetailView.as_view(),
        name='laboratorio_detail'),
    url(
        r'^control/(?P<id>\d+)/laboratorio/editar/$',
        views.LaboratorioView.as_view(),
        name='laboratorio'),
    url(
        r'^(?P<embarazo_id>\d+)/crear-control/$',
        views.ControlCreateView.as_view(),
        name='create'),
    url(
        r'^control/(?P<id>\d+)/data/crecimiento-neonatal/$',
        views.DataCrecimientoNeonatalView.as_view(),
        name='data_crecimiento_neonatal'),
    url(
        r'^control/(?P<id>\d+)/data/altura-uterina/$',
        views.DataAlturaUterinaView.as_view(),
        name='data_altura_uterina'),
    url(
        r'^control/(?P<id>\d+)/data/ganancia-peso-materno/$',
        views.DataGananciaPesoMaternoView.as_view(),
        name='data_ganancia_peso_materno'),
)

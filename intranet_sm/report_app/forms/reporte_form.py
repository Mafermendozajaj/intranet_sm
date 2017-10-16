from django import forms
from functools import partial
from intranet_sm.report_app.models import Reporte

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class ReporteForm(forms.ModelForm):

    class Meta:
        model = Reporte
        fields = ['tipo_reporte', 'observador', 'observadores','fecha_obs', 'asistente', 'proyecto',
        	'telescopio', 'datos', 'horas_trabajadas', 'hp_clima', 'hp_instrumentos',
        	'hp_software', 'vacio_camara', 'vacio_ls', 'vacio_li', 'enviado', 'comentarios']

        widgets = {

            'fecha_obs': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'datepicker', 'placeholder': 'Seleccione una fecha'}),
            'comentarios': forms.Textarea(attrs={'placeholder': 'Comentarios'}),
        }

from django import forms
from functools import partial
from intranet_sm.report_app.models import Reporte

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class ReporteForm(forms.ModelForm):
     class Meta:
         model = Reporte
         fields = ['tipo_reporte','observadores', 'fecha_obs', 'asistente', 'proyecto']

         widgets = {
            'observadores': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'asistente': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'proyecto': forms.RadioSelect(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'tipo_reporte': forms.RadioSelect(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'fecha_obs': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'datepicker', 'placeholder': 'Select a date'}),
            'observador': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'telescopio': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'datos': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'horas_trabajadas': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'hp_clima': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'hp_instrumentos': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'hp_software': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'comentarios': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'vacio_camara': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'vacio_ls': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'vacio_li': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
            'enviado': forms.TextInput(attrs={'class': 'input-xlarge', 'placeholder': 'Observadores'}),
        }

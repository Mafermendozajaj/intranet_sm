from django.apps import AppConfig


class AsistenciaAppConfig(AppConfig):
    name = 'intranet_sm.asistencia_app'
    verbose_name = "Asistencia"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass

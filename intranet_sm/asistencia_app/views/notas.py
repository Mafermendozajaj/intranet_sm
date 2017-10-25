import datetime

from rest_framework import generics

from intranet_sm.asistencia_app.models import Nota
from intranet_sm.asistencia_app.serializers import NotaSerializer


class NotaListApi(generics.ListCreateAPIView):

    serializer_class = NotaSerializer

    def get_queryset(self, *args, **kwargs):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """

        desde = self.request.GET.get('start')
        hasta = self.request.GET.get('end')

        desde = datetime.datetime.strptime(desde, "%Y-%m-%d")
        hasta = datetime.datetime.strptime(hasta, "%Y-%m-%d")

        empleado_id = self.kwargs.get('empleado_id')
        print(empleado_id, desde, hasta)

        return Nota.objects.filter(empleado_id=empleado_id, start__range=[desde, hasta],)


class NotaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

from rest_framework import serializers
from intranet_sm.asistencia_app.models import Nota, Marca


class NotaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nota
        fields = ('title', 'id', 'empleado', 'start', 'end')


class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = ('id', 'id_user', 'dispositivo', 'start', 'title')

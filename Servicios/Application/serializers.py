from rest_framework import serializers
from .models import Usuario, Partida

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'password')

class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partida
        fields = ('id', 'fecha', 'usuario', 'minutos_jugados', 'puntaje')

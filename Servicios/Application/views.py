from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import UsuarioSerializer, PartidaSerializer
from .models import Usuario, Partida

# Create your views here. (Vistas de las entidades)

# Vista de la página principal 
def index(request):
    return HttpResponse("Esta página web es de API para las relaciones de 'Usuario' y 'Partida'")

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PartidaViewSet(viewsets.ModelViewSet):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer

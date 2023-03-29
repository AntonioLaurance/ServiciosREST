from django.db import models

# Create your models here.
class Usuario(models.Model):
    password = models.CharField(max_length = 60)

# Implementa el borrado en cascada por si se borra un usuario también
# se borran todos los datos asociados a este
class Partida(models.Model):
    fecha = models.CharField(max_length = 10)
    usuario = models.ForeignKey(Usuario, null = False, blank = False, on_delete = models.CASCADE)
    minutos_jugados = models.IntegerField()
    puntaje = models.IntegerField()

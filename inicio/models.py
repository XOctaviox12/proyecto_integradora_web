from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Perfil de {self.user.username}'


class Estadisticas(models.Model):
    visitas_home = models.PositiveIntegerField(default=0)
    registros_exitosos = models.PositiveIntegerField(default=0)


class PageVisit(models.Model):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Visitas: {self.count}"
    
class Jugadores(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class ComentarioContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email} ({self.fecha_envio.strftime('%d/%m/%Y %H:%M')})"
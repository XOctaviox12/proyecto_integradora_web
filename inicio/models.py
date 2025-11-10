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
    count = models.IntegerField(default=0)

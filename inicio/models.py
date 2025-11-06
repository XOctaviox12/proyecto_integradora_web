from django.db import models

class Explorador(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.correo})"

    class Meta:
        verbose_name = "Registro de Explorador"
        verbose_name_plural = "Registros de Exploradores"

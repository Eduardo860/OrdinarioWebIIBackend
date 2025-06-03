from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    usuario_creacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_actualizacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

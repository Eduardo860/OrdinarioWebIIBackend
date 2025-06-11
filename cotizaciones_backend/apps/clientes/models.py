from django.db import models

class Cliente(models.Model):
    nombre_contacto = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    usuario_creacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_actualizacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_contacto

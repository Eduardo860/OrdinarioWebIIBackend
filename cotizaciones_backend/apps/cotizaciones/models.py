from django.db import models
from apps.clientes.models import Cliente
from apps.productos.models import Producto

# ---- Catálogos ----

class EstatusCotizacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    usuario_creacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_actualizacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    usuario_creacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_actualizacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Salon(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    capacidad = models.IntegerField(null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    usuario_creacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_actualizacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# ---- Cotizacion ----

class Cotizacion(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_salon = models.ForeignKey(Salon, on_delete=models.SET_NULL, null=True, blank=True)
    id_estatus = models.ForeignKey(EstatusCotizacion, on_delete=models.SET_NULL, null=True, blank=True)
    id_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    notas = models.TextField(null=True, blank=True)
    usuario_creacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_actualizacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Cotización #{self.id} - Cliente: {self.id_cliente.nombre_contacto}"

# ---- DetalleCotizacion ----

class DetalleCotizacion(models.Model):
    id_cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    usuario_creacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_actualizacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.cantidad} x {self.id_producto.nombre} (Cotización #{self.id_cotizacion.id})"

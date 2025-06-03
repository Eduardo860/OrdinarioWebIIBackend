from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)
    usuario_creacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_actualizacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

class Cliente(models.Model):
    nombre_contacto = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=20)
    usuario_creacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_actualizacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    usuario_creacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_actualizacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    usuario_creacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_actualizacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

class EstatusCotizacion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    usuario_creacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_actualizacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, blank=True)
    usuario_creacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario_actualizacion = models.CharField(max_length=100, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)
    estado = models.BooleanField(default=True)

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

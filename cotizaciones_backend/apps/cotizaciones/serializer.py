from rest_framework import serializers
from .models import EstatusCotizacion, MetodoPago, Salon, Cotizacion, DetalleCotizacion
from apps.productos.models import Producto


class EstatusCotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstatusCotizacion
        fields = '__all__'

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'

class SalonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = '__all__'

class CotizacionSerializer(serializers.ModelSerializer):
    # — Para lectura: nombres en lugar de IDs
    cliente_nombre     = serializers.CharField(source='id_cliente.nombre_contacto', read_only=True)
    salon_nombre       = serializers.CharField(source='id_salon.nombre',        read_only=True)
    estatus_nombre     = serializers.CharField(source='id_estatus.nombre',      read_only=True)
    metodo_pago_nombre = serializers.CharField(source='id_metodo_pago.nombre',  read_only=True)

    # — Para escritura: lista de productos
    productos = serializers.ListField(
        child=serializers.DictField(), write_only=True
    )
    # — Para lectura: monto_total calculado
    monto_total = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Cotizacion
        fields = [
            # escritura
            'id_cliente', 'id_salon', 'id_estatus', 'id_metodo_pago',
            'fecha', 'notas', 'usuario_creacion',
            'productos',
            # lectura
            'id', 'fecha', 'notas',
            'cliente_nombre', 'salon_nombre',
            'estatus_nombre', 'metodo_pago_nombre',
            'monto_total',
        ]

    def create(self, validated_data):
        productos_data = validated_data.pop('productos')
        # Creamos con monto_total=0 para no violar NOT NULL
        cot = Cotizacion.objects.create(monto_total=0, **validated_data)
        total = 0
        for item in productos_data:
            prod = Producto.objects.get(pk=item['id_producto'])
            subtotal = prod.precio * item['cantidad']
            DetalleCotizacion.objects.create(
                id_cotizacion=cot,
                id_producto=prod,
                cantidad=item['cantidad'],
                subtotal=subtotal,
                usuario_creacion=validated_data['usuario_creacion']
            )
            total += subtotal

        cot.monto_total = total
        cot.save()
        return cot


class DetalleCotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCotizacion
        fields = '__all__'

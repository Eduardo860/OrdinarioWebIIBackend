from rest_framework import serializers
from .models import EstatusCotizacion, MetodoPago, Salon, Cotizacion, DetalleCotizacion

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
    class Meta:
        model = Cotizacion
        fields = '__all__'

class DetalleCotizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleCotizacion
        fields = '__all__'

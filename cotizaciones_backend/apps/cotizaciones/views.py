from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import EstatusCotizacion, MetodoPago, Salon, Cotizacion, DetalleCotizacion
from .serializer import (
    EstatusCotizacionSerializer,
    MetodoPagoSerializer,
    SalonSerializer,
    CotizacionSerializer,
    DetalleCotizacionSerializer
)

class EstatusCotizacionViewSet(viewsets.ModelViewSet):
    queryset = EstatusCotizacion.objects.filter(estado=True)
    serializer_class = EstatusCotizacionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response({'mensaje': 'Estatus de cotización deshabilitado'}, status=status.HTTP_200_OK)

class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = MetodoPago.objects.filter(estado=True)
    serializer_class = MetodoPagoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response({'mensaje': 'Método de pago deshabilitado'}, status=status.HTTP_200_OK)

class SalonViewSet(viewsets.ModelViewSet):
    queryset = Salon.objects.filter(estado=True)
    serializer_class = SalonSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response({'mensaje': 'Salón deshabilitado'}, status=status.HTTP_200_OK)

class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Cotizacion.objects.filter(estado=True)
    serializer_class = CotizacionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response({'mensaje': 'Cotización deshabilitada'}, status=status.HTTP_200_OK)

class DetalleCotizacionViewSet(viewsets.ModelViewSet):
    queryset = DetalleCotizacion.objects.filter(estado=True)
    serializer_class = DetalleCotizacionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response({'mensaje': 'Detalle de cotización deshabilitado'}, status=status.HTTP_200_OK)

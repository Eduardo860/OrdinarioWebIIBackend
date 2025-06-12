from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import EstatusCotizacion, MetodoPago, Salon, Cotizacion, DetalleCotizacion
from .serializer import (
    EstatusCotizacionSerializer,
    MetodoPagoSerializer,
    SalonSerializer,
    CotizacionSerializer,
    DetalleCotizacionSerializer
)

# ------------------------------
# EstatusCotizacion
# ------------------------------

class EstatusCotizacionViewSet(viewsets.ModelViewSet):
    queryset = EstatusCotizacion.objects.filter(estado=True)
    serializer_class = EstatusCotizacionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response({'mensaje': 'Estatus de cotización deshabilitado'}, status=status.HTTP_200_OK)

# ------------------------------
# MetodoPago
# ------------------------------

class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = MetodoPago.objects.filter(estado=True)
    serializer_class = MetodoPagoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response({'mensaje': 'Método de pago deshabilitado'}, status=status.HTTP_200_OK)

# ------------------------------
# Salon
# ------------------------------

class SalonViewSet(viewsets.ModelViewSet):
    queryset = Salon.objects.filter(estado=True)
    serializer_class = SalonSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response({'mensaje': 'Salón deshabilitado'}, status=status.HTTP_200_OK)

# ------------------------------
# Cotizacion (con count y ultimas)
# ------------------------------
class CotizacionViewSet(viewsets.ModelViewSet):
    # No procesamos token aquí, todo queda abierto
    authentication_classes = []
    permission_classes     = [AllowAny]

    queryset = Cotizacion.objects.filter(estado=True).order_by('-fecha')
    serializer_class = CotizacionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response({'mensaje': 'Cotización deshabilitada'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='count')
    def count(self, request):
        total = Cotizacion.objects.filter(estado=True).count()
        return Response({"total": total})

    @action(detail=False, methods=['get'], url_path='ultimas')
    def ultimas(self, request):
        ultimas = Cotizacion.objects.filter(estado=True).order_by('-fecha')[:5]
        serializer = self.get_serializer(ultimas, many=True)
        return Response(serializer.data)


# ------------------------------
# DetalleCotizacion
# ------------------------------
class DetalleCotizacionViewSet(viewsets.ModelViewSet):
    queryset = DetalleCotizacion.objects.filter(estado=True)
    serializer_class = DetalleCotizacionSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        cot_id = self.request.query_params.get('id_cotizacion')
        if cot_id is not None:
            qs = qs.filter(id_cotizacion=cot_id)
        return qs

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response(
            {'mensaje': 'Detalle de cotización deshabilitado'},
            status=status.HTTP_200_OK
        )

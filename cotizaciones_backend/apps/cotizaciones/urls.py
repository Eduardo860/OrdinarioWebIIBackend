# apps/cotizaciones/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CotizacionViewSet,
    EstatusCotizacionViewSet,
    MetodoPagoViewSet,
    SalonViewSet,
    DetalleCotizacionViewSet
)

router = DefaultRouter()

# 1) Rutas específicas PRIMERO
router.register(r'estatus-cotizacion', EstatusCotizacionViewSet)
router.register(r'metodos-pago', MetodoPagoViewSet)
router.register(r'salones', SalonViewSet)
router.register(r'detalle-cotizacion', DetalleCotizacionViewSet, basename='detalle-cotizacion')

# 2) Ruta “catch-all” de cotizaciones al FINAL
router.register(r'', CotizacionViewSet, basename='cotizaciones')

urlpatterns = [
    path('', include(router.urls)),
]

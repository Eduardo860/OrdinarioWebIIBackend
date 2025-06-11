from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstatusCotizacionViewSet, MetodoPagoViewSet, SalonViewSet

router = DefaultRouter()
router.register(r'estatus-cotizacion', EstatusCotizacionViewSet)
router.register(r'metodos-pago', MetodoPagoViewSet)
router.register(r'salones', SalonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

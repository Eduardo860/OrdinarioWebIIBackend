from django.contrib import admin
from .models import EstatusCotizacion, MetodoPago, Salon, Cotizacion, DetalleCotizacion

admin.site.register(EstatusCotizacion)
admin.site.register(MetodoPago)
admin.site.register(Salon)
admin.site.register(Cotizacion)
admin.site.register(DetalleCotizacion)

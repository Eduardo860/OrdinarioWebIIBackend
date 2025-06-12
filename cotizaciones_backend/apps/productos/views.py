from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Producto
from .serializer import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.filter(estado=True)
    serializer_class = ProductoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response({'mensaje': 'Producto deshabilitado correctamente'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='count')
    def count(self, request):
        total = Producto.objects.filter(estado=True).count()
        return Response({"total": total})

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cliente
from .serializer import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.filter(estado=True)
    serializer_class = ClienteSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response({'mensaje': 'Cliente deshabilitado correctamente'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='count')
    def count(self, request):
        total = Cliente.objects.filter(estado=True).count()
        return Response({"total": total})

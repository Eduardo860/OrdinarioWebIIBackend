from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Categoria
from .serializer import CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.filter(estado=True)
    serializer_class = CategoriaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.save()
        return Response({'mensaje': 'Categoría deshabilitada correctamente'}, status=status.HTTP_200_OK)

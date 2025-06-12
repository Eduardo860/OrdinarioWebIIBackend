from rest_framework import serializers
from .models import Usuario
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password

# Serializer para CRUD de usuarios (GET / POST / PUT / DELETE)
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

# Serializer para login con token (POST /api/token/)
class CustomTokenObtainPairSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            usuario = Usuario.objects.get(email=email, estado=True)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError("Credenciales inválidas")

        if not check_password(password, usuario.password):
            raise serializers.ValidationError("Credenciales inválidas")

        # Generamos manualmente los tokens
        refresh = RefreshToken.for_user(usuario)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'usuario': {
                'id': usuario.id,
                'nombre': usuario.nombre,
                'email': usuario.email
            }
        }

        return data

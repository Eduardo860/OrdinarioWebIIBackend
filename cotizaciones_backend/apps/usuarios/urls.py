from django.urls import path
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),  # POST /api/usuarios/login/
]

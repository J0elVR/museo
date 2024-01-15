from django.urls import path
from .views import organizar_expediente, buscar_expedientes

urlpatterns = [
    path('organizar/<int:expediente_id>/', organizar_expediente, name='organizar_expediente'),
    path('buscar/', buscar_expedientes, name='buscar_expedientes'),
]

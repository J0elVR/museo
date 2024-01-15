from django.urls import path
from .views import crear_expediente, lista_expedientes

urlpatterns = [
    path('crear/', crear_expediente, name='crear_expediente'),
    path('lista/', lista_expedientes, name='lista_expedientes'),
]

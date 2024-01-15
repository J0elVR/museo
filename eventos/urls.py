from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('eventos/', views.eventos_museo, name='eventos_museo'),  
    path('ver_evento/', views.ver_evento, name='ver_evento'),  
    path('reservar_evento/', views.reservar_evento, name='reservar_evento'),  
]

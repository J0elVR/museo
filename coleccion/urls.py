from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),
    path('colecciones/', views.colecciones_museo, name='colecciones_museo'),
    path('mesoamerica/', views.coleccion_meso, name='coleccion_meso'),
    path('colonia/', views.coleccion_colonia, name='coleccion_colonia'),
    path('maestros/', views.coleccion_maestros, name='coleccion_maestros'),
    path('romanticismo/', views.coleccion_romanticismo, name='coleccion_romanticismo'),
]
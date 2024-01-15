from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='pagina_inicio'),  
    path('admin/', admin.site.urls),
    path('empleados/', include('empleados.urls')),
    path('info/', include('info.urls')),
    path('historia/', include('historia.urls')),
    path('eventos/', include('eventos.urls')),
    path('coleccion/', include('coleccion.urls')),
    path('organizador/', include('organizador.urls')),
    path('expedientes/', include('expedientes.urls')),
]

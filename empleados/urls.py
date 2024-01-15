from django.urls import path, include
from . import views
from .views import registrar_empleado, pagina_inicio, lista_empleados, admin_museo

urlpatterns = [
    path('registrar/', registrar_empleado, name='registrar_empleado'),
    path('', pagina_inicio, name='pagina_inicio'),
    path('lista_empleados/', lista_empleados, name='lista_empleados'),
    path('admin_museo/', admin_museo, name='admin_museo'),  
]

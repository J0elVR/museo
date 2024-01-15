from django.urls import path, include
from . import views
from .views import pagina_inicio, info_museo

urlpatterns = [
    path('', pagina_inicio, name='pagina_inicio'),
    path('info/', views.info_museo, name='info_museo'),
]
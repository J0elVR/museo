from django.urls import path, include
from . import views
from .views import pagina_inicio, historia_museo

urlpatterns = [
    path('', pagina_inicio, name='pagina_inicio'),
    path('historia/', views.historia_museo, name='historia_museo'),
]
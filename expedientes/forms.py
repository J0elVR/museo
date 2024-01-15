from django import forms
from .models import Expediente

class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ['nombre', 'direccion', 'curriculum_vitae', 'foto_identificacion']

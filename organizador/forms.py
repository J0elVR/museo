from django import forms
from .models import Organizador

class OrganizadorForm(forms.ModelForm):
    class Meta:
        model = Organizador
        fields = ['palabras_clave']

from dataclasses import fields
from django import forms
from .models import Reservar

class ReservarForm(forms.ModelForm):
    class Meta:
        model = Reservar
        exclude = ['evento']
        fields = ['nombre']
        
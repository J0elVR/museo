from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'direccion', 'telefono', 'email', 'curp']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input-nombre'}),
            'direccion': forms.TextInput(attrs={'class': 'input-direccion'}),
            'telefono': forms.TextInput(attrs={'class': 'input-telefono'}),
            'email': forms.EmailInput(attrs={'class': 'input-email'}),
            'curp': forms.TextInput(attrs={'class': 'input-curp'}),
        }
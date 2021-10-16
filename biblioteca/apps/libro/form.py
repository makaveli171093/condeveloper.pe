from django import forms

from biblioteca.apps.libro.models import Autor
from .models import Autor


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
            'nombre',
            'apellidos',
            'nacionalidad',
            'correo',
            'descripcion'
        ]
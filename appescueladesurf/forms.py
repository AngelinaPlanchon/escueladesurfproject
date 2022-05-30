from django import forms
from .models import Alumnos


class AlumnoFormulario(forms.Form):
    nombre =forms.CharField()
    apellido =forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    numeroalumno=forms.IntegerField()

  
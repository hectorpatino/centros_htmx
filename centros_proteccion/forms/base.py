
from django import forms
from django.forms import ModelForm
from centros_proteccion.models import RepresentanteLegal, RazonSocial, CentroAtencion


class RepresentanteLegalForm(ModelForm):
    class Meta:
        model = RepresentanteLegal
        fields = ['cedula', 'primer_nombre', 'segundo_nombre', 'primer_apellido',
                   'segundo_apellido', 'telefono', 'correo', 'direccion', 'muni_residencia']









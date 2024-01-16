
from django import forms
from django.forms import ModelForm
from django.urls import reverse_lazy, reverse

from centros_proteccion.models import RepresentanteLegal, RazonSocial, CentroAtencion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div


class RepresentanteLegalForm(ModelForm):
    class Meta:
        model = RepresentanteLegal
        fields = ['cedula', 'primer_nombre', 'segundo_nombre', 'primer_apellido',
                   'segundo_apellido', 'telefono', 'correo', 'direccion', 'muni_residencia']

    def __init__(self, *args, **kwargs):
        is_add = kwargs.pop('is_add', True)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        if is_add:
            self.helper.add_input(Submit('submit', 'Guardar'))
        else:
            self.helper.add_input(Submit('submit', 'Actualizar'))
        self.helper.layout = Layout(
            Fieldset(
                'Información Personal',
                Div('cedula'),
                Div(
                    'primer_nombre',
                    'segundo_nombre',
                    'primer_apellido',
                    'segundo_apellido',
                )
            ),
            Fieldset(
                'Información de Contacto',
                'telefono',
                'correo',
                'direccion',
                'muni_residencia',
            ),
        )


from factory.django import DjangoModelFactory
from factory import Faker, SubFactory

from centros_proteccion.models import RepresentanteLegal
from centros_proteccion.tests.factories.espaciales import MunicipioFactory


class RepresentanteLegalFactory(DjangoModelFactory):
    class Meta:
        model = RepresentanteLegal
        django_get_or_create = (
            'cedula',
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apellido',
            'muni_residencia',
            'direccion',
            'telefono',
            'celular',
            'correo',
            'usuario_registro',
        )

    cedula = Faker('ean8')
    primer_nombre = Faker('first_name')
    segundo_nombre = Faker('first_name')
    primer_apellido = Faker('last_name')
    segundo_apellido = Faker('last_name')
    muni_residencia = SubFactory(MunicipioFactory)
    direccion = Faker('address')
    telefono = Faker('phone_number')
    celular = Faker('phone_number')
    correo = Faker('email')
    usuario_registro = None

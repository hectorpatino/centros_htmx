from factory.django import DjangoModelFactory
import factory
from faker import Faker

from centros_proteccion.models import Provincia, Red, Municipio
faker_ins = Faker()

class ProvinciaFactory(DjangoModelFactory):
    class Meta:
        model = Provincia
        django_get_or_create = (
            'nombre',
        )

    nombre = factory.Faker('city')


class RedFactory(DjangoModelFactory):
    class Meta:
        model = Red
        django_get_or_create = (
            'nombre',
        )

    nombre = factory.Faker('city')


class MunicipioFactory(DjangoModelFactory):
    class Meta:
        model = Municipio
        django_get_or_create = (
            'nombre',
            'codigo',
            'provincia',
            'red',
            'categoria'
        )

    nombre = factory.Faker('city')
    codigo = faker_ins.bban()[0:5]
    provincia = factory.SubFactory(ProvinciaFactory)
    red = factory.SubFactory(RedFactory)
    categoria = 1


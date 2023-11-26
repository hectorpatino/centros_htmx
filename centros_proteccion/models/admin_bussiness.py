from django.contrib.auth import get_user_model
from django.contrib.gis.db import models

from centros_proteccion.models.espaciales import Municipio
from users.models.CustomUser import UsuarioDateTime


class PermisosAdministrativos(UsuarioDateTime):
    class Meta:
        abstract = True
        permissions = (
            ('ver_permisos_administrativos', 'Puede ver los permisos administrativos'),
            ('modificar_permisos_administrativos', 'Puede modificar los permisos administrativos'),
            ('crear_permisos_administrativos', 'Puede crear los permisos administrativos'),
            ('eliminar_permisos_administrativos', 'Puede eliminar los permisos administrativos'),
        )


class Estandarizacion(PermisosAdministrativos):
    # TODO realizar pruebas para que no se queden valores sin aceptar.
    #  es decir si un valor es 69.9 el siguiente no puede ser 70.
    #  si un valor es 70 el otro no puede ser 69.9
    # TODO max value no puede ser nulo
    max_value = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        null=True,
    )
    semaforo = models.CharField(max_length=50)
    nivel_riesgo = models.CharField(max_length=50)
    observaciones = models.TextField(null=False)
    concepto = models.TextField(null=True)

    def __str__(self):
        return self.semaforo

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['max_value'], name='Los valores tiene que ser únicos.'),
            models.UniqueConstraint(fields=['semaforo'], name='El valor del semáforo tiene que ser único.'),
            models.UniqueConstraint(fields=['nivel_riesgo'], name='El nivel de riesgo tiene que ser único.'),
        ]
        permissions = (('ver_estandarizacion', 'Puede ver la estandarización'),
                       ('modificar_estandarizacion', 'Puede modificar la estandarización'),)


class PonderacionColumna(PermisosAdministrativos):
    criterio = models.TextField(null=False, blank=False)
    # TODO la suma de los campos no puede ser mayor a 100
    campo = models.CharField(
        null=False,
        max_length=100,
        blank=False
    )
    ponderacion = models.DecimalField(
        help_text='ponderacion',
        max_digits=2,
        decimal_places=2
    )


class UsuarioMunicipio(PermisosAdministrativos):
    usuario = models.ForeignKey(
        get_user_model(),
        on_delete=models.RESTRICT,
        null=False,
        related_name='usurio_centro',
    )
    municipio = models.ForeignKey(
        Municipio,
        on_delete=models.RESTRICT,
        related_name='usuarios_municipio',
        null=True
    )

    def __str__(self):
        return f'{self.usuario.email} - {self.municipio.nombre}'

    class Meta:
        verbose_name = 'Usuario - Municipio'
        verbose_name_plural = 'Usuarios - Municipios'


class DiferenciacionGenero(UsuarioDateTime):
    hombres = models.IntegerField(null=True, blank=True)
    mujeres = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True

from django.contrib.gis.db import models
from django.core.exceptions import ValidationError

from centros_proteccion.models.dominios import DTipoPersona, DModalidad, DArea, DCondicion
from centros_proteccion.models.espaciales import Municipio
from users.models.CustomUser import UsuarioDateTime


class RepresentanteLegal(UsuarioDateTime):
    cedula = models.CharField(max_length=50, null=False, blank=False
                              , help_text='Cédula del representante legal')
    primer_nombre = models.CharField(max_length=50, null=False, blank=False)
    segundo_nombre = models.CharField(max_length=50, null=True, blank=True)
    primer_apellido = models.CharField(max_length=50, null=False, blank=False)
    segundo_apellido = models.CharField(max_length=50, null=True, blank=True)
    muni_residencia = models.ForeignKey(
        Municipio,
        on_delete=models.RESTRICT,
        related_name='representante_legal',
        null=True
    )
    direccion = models.CharField(max_length=250, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    celular = models.CharField(max_length=50, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f'{self.primer_apellido} {self.primer_nombre} - {self.cedula}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['cedula'], name='cédula única'),
        ]
        ordering = ['primer_apellido', 'primer_nombre']
        verbose_name_plural = 'Representantes Legales'
        verbose_name = 'Representante Legal'
        permissions = (('ver_representante_legal', 'Puede ver el representante legal'),
                       ('modificar_representante_legal', 'Puede modificar el representante legal'),
                       ('crear_representante_legal', 'Puede crear el representante legal'),
                       ('eliminar_representante_legal', 'Puede eliminar el representante legal'),)


class RazonSocial(UsuarioDateTime):
    nit = models.CharField(max_length=20, null=False, blank=False)
    nombre = models.CharField(max_length=250, null=False, blank=False, default='')
    tipo_persona = models.ForeignKey(
        DTipoPersona,
        on_delete=models.RESTRICT,
        related_name='razon_social',
        null=True
    )
    representante_legal = models.ForeignKey(
        RepresentanteLegal,
        on_delete=models.RESTRICT,
        related_name='razon_social',
        null=True
    )

    class Meta:
        verbose_name = 'Razon social'
        verbose_name_plural = 'Razones Sociales'

        constraints = [
            models.UniqueConstraint(fields=['nit'], name='nit_unique_constrain')
        ]
        permissions = (
            ('ver_razon_social', 'Puede ver la razón social'),
            ('modificar_razon_social', 'Puede modificar la razón social'),
            ('crear_razon_social', 'Puede crear la razón social'),
            ('eliminar_razon_social', 'Puede eliminar la razón social'),
        )

    def __str__(self):
        return f'{self.nit} - {self.nombre}'

    def clean(self):
        if self.representante_legal is None:
            raise ValidationError('El representante legal no puede ser nulo')


class CentroAtencion(UsuarioDateTime):
    razon_social = models.ForeignKey(
        RazonSocial,
        related_name='centros_razon',
        null=True,
        on_delete=models.RESTRICT,
        blank=False,
        verbose_name='razon social',
    )
    municipio = models.ForeignKey(
        Municipio,
        related_name='centros',
        null=False,
        on_delete=models.RESTRICT,
        verbose_name='municipio',
        blank=False
    )
    modalidad = models.ForeignKey(
        DModalidad,
        related_name='modalidad',
        null=True,
        on_delete=models.RESTRICT,
        verbose_name='modalidad',
        blank=False
    )

    sede = models.CharField(max_length=250, null=False, blank=False)
    # fecha_apertura = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=250, blank=True, null=False)
    area = models.ForeignKey(
        DArea,
        on_delete=models.RESTRICT,
        null=True,
        blank=False
    )
    fecha_cierre = models.DateField(null=True, blank=True)
    # geom = models.PointField(srid=4326, null=True)
    pagina_web = models.URLField(null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)

    # TODO verificar la nulidad por sp
    condicion = models.ForeignKey(DCondicion, on_delete=models.RESTRICT, null=True, blank=False)
    creado_pqr = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f'{self.modalidad.nombre} - {self.municipio} - {self.sede}'

    class Meta:
        verbose_name = 'Centro atención'
        verbose_name_plural = 'Centros de atención'
        permissions = (
            ('ver_centro_atencion', 'Puede ver el centro de atención'),
            ('crear_centro_atencion', 'Puede crear el centro de atención'),
            ('modificar_centro_atencion', 'Puede modificar el centro de atención'),
            ('eliminar_centro_atencion', 'Puede eliminar el centro de atención'),
            ('crear_centro_atencion_pqr', 'Puede crear el centro de atención desde el pqr'),
        )


class TipoPersonaRazonSocial(UsuarioDateTime):
    razon_social = models.OneToOneField(
        RazonSocial,
        related_name='tipos_persona',
        null=False,
        on_delete=models.RESTRICT,
        blank=False,
        verbose_name='razon social',
    )
    tipo_persona = models.ForeignKey(
        DTipoPersona,
        related_name='tipos_persona',
        null=False,
        on_delete=models.RESTRICT,
        blank=False,
        verbose_name='tipo persona',
    )


class CorreoElectronico(UsuarioDateTime):
    centro_proteccion = models.ForeignKey(
        CentroAtencion,
        related_name='correos',
        null=False,
        blank=False,
        on_delete=models.RESTRICT
    )
    correo = models.EmailField(unique=True)


class NumerosTelefono(UsuarioDateTime):
    centro_proteccion = models.ForeignKey(
        CentroAtencion,
        related_name='telefonos',
        null=False,
        blank=False,
        on_delete=models.RESTRICT
    )
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.numero

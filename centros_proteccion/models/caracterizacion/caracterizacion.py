from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from centros_proteccion.models.dominios import DConceptoSanitario, DServicios, DExigencias, DAdministrador, \
    DInstitucion, DFinanciamiento, DServiciosSalud, DProfesionalSalud, DEnfoqueDiferencial, DSubsidio, \
    DActividadesFamiliares
from users.models.CustomUser import UsuarioDateTime
from .base import AbstractCaracterizacion
from centros_proteccion.models.base import CentroAtencion


class Caracterizacion(AbstractCaracterizacion):
    """
    Caracterización de los centros de protección.
    """
    centro_atencion = models.ForeignKey(
        CentroAtencion,
        related_name='registros',
        null=False,
        blank=False,
        on_delete=models.RESTRICT
    )
    activo = models.BooleanField(default=True, null=True, blank=False)
    # TODO esto creo que no va acá
    mas_dos_sedes = models.BooleanField(default=False, null=True, blank=False)
    # QUESTION el campo concepto_sanitario para ce que no debería ir acá.
    concepto_sanitario = models.ForeignKey(DConceptoSanitario, on_delete=models.RESTRICT, null=True, blank=False)

    # 2.3 CV - 1.18 CLE
    servicios = models.ManyToManyField(DServicios, blank=True)

    # region cantidades residentes

    residentes_femeninos = models.IntegerField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000000)]
    )
    mujeres_menores_59 = models.IntegerField(
        null=True,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000000)]
    )
    mujeres_60_69 = models.IntegerField(null=True, blank=True,
                                        validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    mujeres_70_79 = models.IntegerField(null=True, blank=True,
                                        validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    mujeres_80_89 = models.IntegerField(null=True, blank=True,
                                        validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    mujeres_90_99 = models.IntegerField(null=True, blank=True,
                                        validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    mujeres_100_mas = models.IntegerField(null=True, blank=True,
                                          validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    hombres_menores_59 = models.IntegerField(null=True, blank=True,
                                             validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    hombres_60_69 = models.IntegerField(null=True, blank=True,
                                        validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    hombres_70_79 = models.IntegerField(null=True, blank=True,
                                        validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    hombres_80_89 = models.IntegerField(null=True, blank=True,
                                        validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    hombres_90_99 = models.IntegerField(null=True, blank=True,
                                        validators=[MinValueValidator(0), MaxValueValidator(1000000)])
    hombres_100_mas = models.IntegerField(null=True, blank=True,
                                          validators=[MinValueValidator(0), MaxValueValidator(1000000)])

    residentes_masculinos = models.IntegerField(
        null=True,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000000)]
    )
    residentes_otros_generos = models.IntegerField(
        null=True,
        blank=False,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000000)]
    )
    # endregion

    exigencias = models.ManyToManyField(DExigencias, blank=True, related_name='centros')

    # 3 CV - 1.20 CLE
    # TODO verificar que no sea null en la base de datos
    objeto = models.CharField(max_length=50, help_text='Objeto del centro', null=True, blank=True)

    observacion = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    # region 1.19 CV - 1.15 CLE
    atencion_domiciliaria = models.BooleanField(
        default=False,
        null=True,
        help_text='El centro ofrece atención domiciliaria',
    )
    tele_asistencia = models.BooleanField(
        default=False,
        null=True,
        help_text='El centro ofrece tele asistencia',
    )

    # region CV 1.20 - CLE 1.17
    administrador = models.ForeignKey(
        DAdministrador,
        related_name='centros_administrados',
        null=True,
        blank=False,
        on_delete=models.RESTRICT
    )

    # endregion

    def __str__(self):
        return f'{self.centro_atencion.sede}'

    class Meta:
        verbose_name = 'Caracterización Poblacional'
        verbose_name_plural = 'Caracterización Poblacional'


class CentroAInstitucion(AbstractCaracterizacion):
    # 1.24 CV - 4 CLE
    caracterizacion = models.ForeignKey(
        Caracterizacion,
        related_name='instituciones',
        null=False,
        blank=False,
        on_delete=models.RESTRICT
    )
    institucion = models.ForeignKey(
        DInstitucion,
        related_name='centros',
        null=False,
        blank=False,
        on_delete=models.RESTRICT
    )
    actividad = models.TextField(null=False, blank=True, max_length=1000)

    class Meta:
        verbose_name = 'Centro a institución'
        verbose_name_plural = 'Centros a instituciones'

    def __str__(self):
        return f'{self.centro_atencion} - {self.institucion}'


class CaracterizacionFinanciador(AbstractCaracterizacion):
    # 1.23 CVV 9 CLE
    caracterizacion = models.ForeignKey(
        Caracterizacion, on_delete=models.RESTRICT, related_name='car_financiadores', null=False, blank=False)
    financiador = models.ForeignKey(
        DFinanciamiento, on_delete=models.RESTRICT, related_name='car_financiadores', null=False, blank=False)


class ServiciosSaludCarac(AbstractCaracterizacion):
    # 1.21 CV 5 CLE
    caracterizacion = models.ForeignKey(
        Caracterizacion, on_delete=models.RESTRICT, related_name='car_serv_salud', null=False, blank=False)
    servicios_salud = models.ForeignKey(
        DServiciosSalud, on_delete=models.RESTRICT, related_name='car_serv_salud', null=False, blank=False)
    habilitado = models.BooleanField(null=True)


class ProfesionalSaludCarac(AbstractCaracterizacion):
    caracterizacion = models.ForeignKey(
        Caracterizacion, on_delete=models.RESTRICT, related_name='caracterizacion_profesional_salud', null=False,
        blank=False)
    # 1.22 CV - 6 CLS
    profesional = models.ForeignKey(
        DProfesionalSalud, on_delete=models.RESTRICT, related_name='caracterizacion_profesional_salud', null=False,
        blank=False)
    cantidad = models.IntegerField(null=True, blank=True)


class CaracterizacionEnfDif(AbstractCaracterizacion):
    # 2.3 CV - 12 CLE
    caracterizacion = models.ForeignKey(
        Caracterizacion, on_delete=models.RESTRICT, related_name='caracterizacion_enfoque_diferencial', null=False,
    )
    enfoque = models.ForeignKey(
        DEnfoqueDiferencial, on_delete=models.RESTRICT, related_name='caracterizacion_enfoque_diferencial', null=False,
    )


class CaracterizacionSubsidio(AbstractCaracterizacion):
    # 2.4 CV - 13 CLE
    caracterizacion = models.ForeignKey(
        Caracterizacion, on_delete=models.RESTRICT, related_name='caracterizacion_subsidio', null=False, blank=False)
    subsidio = models.ForeignKey(
        DSubsidio, on_delete=models.RESTRICT, related_name='caracterizacion_subsidio', null=False, blank=False)


class ActividadesFamiliaresLE(UsuarioDateTime):
    # 2.5 CV
    caracterizacioncv = models.ForeignKey(
        Caracterizacion, on_delete=models.RESTRICT, related_name='actividades_familiares', null=False, blank=False)
    actividad_familiar = models.ForeignKey(
        DActividadesFamiliares, on_delete=models.RESTRICT, related_name='actividades_familiares', null=False,
        blank=False)


class CaracterizacionLE(UsuarioDateTime):
    """
    Caracterización de larga estancia
    """
    caracterizacion = models.ForeignKey(
        Caracterizacion, on_delete=models.RESTRICT, related_name='caracterizacion_le', null=False, blank=False)


class CaracExigeOtras(UsuarioDateTime):
    caracterizacion = models.ForeignKey(
        Caracterizacion, on_delete=models.RESTRICT, related_name='otras_exigencias', null=False, blank=False
    )
    exigencia = models.CharField(max_length=100, null=False, blank=False)

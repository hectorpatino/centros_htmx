from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .base import AbstractCaracterizacion
from .caracterizacion import Caracterizacion
from ..dominios import DConceptoSanitario


class CaracterizacionCV(AbstractCaracterizacion):
    caracterizacion = models.ForeignKey(
        Caracterizacion, on_delete=models.RESTRICT, related_name='caracterizacion_cv', null=False, blank=False)
    # 1.11 CV
    cantidad_centros_municipio = models.IntegerField(null=True, blank=True)
    # region 1.12 CV
    cantidad_privados = models.IntegerField(null=True, blank=True)
    cantidad_publicos = models.IntegerField(null=True, blank=True)
    # endregion

    # region 1.13 CV
    cantidad_urbanos = models.IntegerField(null=True, blank=True)
    cantidad_rurales = models.IntegerField(null=True, blank=True)
    # endregion

    # region 1.15 CV - 1.16 CV
    dias_mes = models.IntegerField(null=True, blank=True,
                                   validators=[MinValueValidator(0), MaxValueValidator(31)])

    dias_semana = models.IntegerField(null=True, blank=True,
                                      validators=[MinValueValidator(0), MaxValueValidator(7)])
    # endregion

    # region 1.17 CV
    cuenta_resolucion = models.BooleanField(default=False, null=True,
                                            help_text='El centro cuenta con resolución de habilitación')
    resolucion = models.CharField(max_length=150, null=True)
    # endregion

    # region 1.18 CV
    # TODO falta añadir la fecha de la visita.
    visita_ivc = models.BooleanField(default=False, null=True,
                                     help_text='El centro ha sido visitado por el Inspección Vigilancia Control', )
    concepto_previo = models.ForeignKey(DConceptoSanitario, on_delete=models.RESTRICT, null=True, blank=True)
    fecha_visita = models.DateField(null=True, blank=True)
    # endregion

    # region 2.1 CV - 2.2 CV
    beneficiario_estampilla = models.IntegerField(
        null=True,
        blank=True,
        help_text='Cuantas personas mayores son beneficiarias del recurso de estampilla en el centro.',
    )
    no_beneficiario_estampilla = models.IntegerField(
        null=True,
        blank=True,
        help_text='Cuantas personas mayores no son beneficiarias del recurso de estampilla en el centro.',
    )
    # endregion

    class Meta:
        verbose_name = 'Caracterización de centros de vida'
        verbose_name_plural = 'Caracterización de centros de vida'
        permissions = (
            ('ver_caracterizacion_centro_vida', 'Puede ver la caracterización de centros de vida'),
            ('modificar_caracterizacion_centro_vida', 'Puede modificar la caracterización de centros de vida'),
            ('crear_caracterizacion_centro_vida', 'Puede crear la caracterización de centros de vida'),
            ('eliminar_caracterizacion_centro_vida', 'Puede eliminar la caracterización de centros de vida',)
        )

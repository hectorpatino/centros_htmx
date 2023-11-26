from .base import Dominios


class DExigencias(Dominios):
    class Meta:
        verbose_name = 'Exigencia'
        verbose_name_plural = 'Exigencias'


class DInstitucion(Dominios):
    class Meta:
        verbose_name = 'Institución'
        verbose_name_plural = 'Instituciones'


class DTipoPersona(Dominios):
    class Meta:
        verbose_name = 'Tipo de persona'
        verbose_name_plural = 'Tipos de personas'


class DActividadesFamiliares(Dominios):
    class Meta:
        verbose_name = 'Actividad familiar'
        verbose_name_plural = 'Actividades familiares'


class DCondicion(Dominios):
    class Meta:
        verbose_name = 'Condición'
        verbose_name_plural = 'Condiciones'


class DConceptoSanitario(Dominios):
    class Meta:
        verbose_name = 'Concepto sanitario'
        verbose_name_plural = 'Conceptos sanitarios'


class DServiciosSalud(Dominios):
    class Meta:
        verbose_name = 'Servicio de salud'
        verbose_name_plural = 'Servicios de salud'


class DServicios(Dominios):
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'


class DProfesionalSalud(Dominios):
    class Meta:
        verbose_name = 'Profesional de la salud'
        verbose_name_plural = 'Profesionales de la salud'


class DFinanciamiento(Dominios):
    class Meta:
        verbose_name = 'Financiamiento'
        verbose_name_plural = 'Financiamientos'


class DSubsidio(Dominios):
    class Meta:
        verbose_name = 'Subsidio'
        verbose_name_plural = 'Subsidios'


class DAdministrador(Dominios):
    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'



class DArea(Dominios):
    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'


class DEnfoqueDiferencial(Dominios):
    class Meta:
        verbose_name = 'Enfoque diferencial'
        verbose_name_plural = 'Enfoques diferenciales'


class DModalidad(Dominios):
    class Meta:
        verbose_name = 'Modalidad'
        verbose_name_plural = 'Modalidades'

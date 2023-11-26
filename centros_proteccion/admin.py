from django.contrib import admin


from centros_proteccion.models import (Provincia, Red, Municipio, DAdministrador, DArea, DConceptoSanitario, DCondicion,
                                       DServicios, DServiciosSalud, Caracterizacion, CentroAtencion, DModalidad)

admin.site.register(DAdministrador)
admin.site.register(DArea)
admin.site.register(DConceptoSanitario)
admin.site.register(DCondicion)
admin.site.register(DServicios)
admin.site.register(DServiciosSalud)
admin.site.register(DModalidad)

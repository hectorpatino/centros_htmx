from django.contrib.gis.db import models

from users.models.CustomUser import UsuarioDateTime


class DiferenciacionGenero(UsuarioDateTime):
    hombres = models.IntegerField(null=True, blank=True)
    mujeres = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True



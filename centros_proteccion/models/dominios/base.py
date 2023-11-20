from django.contrib.gis.db import models


class Dominios(models.Model):
    nombre = models.CharField(max_length=150, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombre

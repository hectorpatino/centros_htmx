from django.contrib.gis.db import models


class Provincia(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    geom = models.PolygonField(srid=4326, null=True)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


class Red(models.Model):
    nombre = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326, null=True)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, related_name='municipios',
                                 on_delete=models.RESTRICT, null=True)
    codigo = models.CharField(max_length=5)
    geom = models.MultiPolygonField(srid=4326, null=True)
    red = models.ForeignKey(Red, related_name='municipios',
                            on_delete=models.RESTRICT, null=True)
    # TODO no puede ser falso toca arregla SP
    categoria = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ('nombre',)
        verbose_name = 'municipio'
        verbose_name_plural = 'municipios'

    def __str__(self):
        return f'{self.nombre}'

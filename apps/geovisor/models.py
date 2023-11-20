from django.contrib.gis.db import models

# Create your models here.
class Predio(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    npn = models.CharField(max_length=30)
    numero_predial = models.CharField(max_length=20,null=True)
    municipio = models.TextField(null=True)
    departamento = models.TextField(null=True)
    direccion  = models.TextField(null=True)
    destinacion_economica = models.TextField(null=True)
    Tipo = models.TextField(null=True)


    # Returns the string representation of the model.
    def __str__(self):
        return self.npn

class Terreno(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    npn = models.CharField(max_length=30)
    numero_predial = models.CharField(max_length=20,null=True)
    area_digitada = models.FloatField(null=True)
    area_cartografica = models.FloatField(null=True)
     # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = models.MultiPolygonField(srid=4326,null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.npn

class construccion(models.Model):
    npn = models.CharField(max_length=30)
    numero_predial = models.CharField(max_length=40,null=True)
    identificador = models.TextField(null=True)
    planta_ubicacion =  models.IntegerField(null=True)
    total_habitaciones = models.IntegerField(null=True)
    total_banios = models.IntegerField(null=True)
    total_locales = models.IntegerField(null=True)
    total_pisos =  models.IntegerField(null=True)
    anio_construccion =  models.IntegerField(null=True)
    avaluo =  models.FloatField(null=True)
    area_construida =  models.FloatField(null=True)
    area_cartografica =  models.FloatField(null=True)
    uso = models.TextField(null=True)
    geom = models.MultiPolygonField(srid=4326,null=True)
  
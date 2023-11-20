from django.contrib.gis.db import models

# Create your models here.
class Predio(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    npn = models.CharField(max_length=30)
    numero_predial = models.CharField(max_length=20,null=True)
    destino = models.TextField(null=True)
    orip = models.CharField(max_length=3,null=True)
    matricula = models.TextField(null=True)
    area_terreno_digitada = models.FloatField(null=True)
    area_construida_digitada = models.FloatField(null=True)
    area_cartografica = models.FloatField(null=True)
    municipio = models.TextField(null=True)
    departamento = models.TextField(null=True)
    estado = models.IntegerField(null=True)
    direccion  = models.TextField(null=True)
    vigencia = models.IntegerField(null=True)
    comienzo_vida_util = models.DateField(null=True)
    fin_vida_util = models.DateField(null=True)

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
    comienzo_vida_util = models.DateField(null=True)
    fin_vida_util = models.DateField(null=True)
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = models.MultiPolygonField(srid=4686,null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.npn

class Unidades(models.Model):
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
    comienzo_vida_util = models.DateField(null=True)
    fin_vida_util = models.DateField(null=True)

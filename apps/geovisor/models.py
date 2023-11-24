from re import T
from django.contrib.gis.db import models

# Create your models here.
class Predio(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    npn = models.CharField(max_length=30)
    numero_predial = models.CharField(max_length=20,null=True)
    direccion  = models.TextField(null=True)
    tipo = models.TextField(null=True)
    condicion = models.TextField(null=True)
    destinacion_economica = models.TextField(null=True)
    clase_suelo = models.TextField(null=True)
        
    # Returns the string representation of the model.
    def __str__(self):
        return self.npn

class Terreno(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    npn = models.CharField(max_length=30)
    numero_predial = models.CharField(max_length=20,null=True)
    area_digitada = models.FloatField(null=True)
    codigo_manzana = models.TextField(null=True)
    lale = models.TextField(null=True)
     # GeoDjango-specific: a geometry field (MultiPolygonField)   
    geom = models.MultiPolygonField(srid=4326,null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.npn

class Construccion(models.Model):
    npn = models.CharField(max_length=30)
    numero_predial = models.CharField(max_length=40,null=True)
    identificador = models.TextField(null=True)
    tipo_construccion = models.TextField(null=True)
    tipo_dominio = models.TextField(null=True)
    numero_pisos= models.IntegerField(null=True)
    numero_sotanos= models.IntegerField(null=True)
    numero_mezanines= models.IntegerField(null=True)
    numero_semisotanos= models.IntegerField(null=True)
    area_construida = models.FloatField(null=True)
    geom = models.MultiPolygonField(srid=4326,null=True)

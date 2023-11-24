from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from apps.geovisor.models import Terreno, Construccion, Predio

class TerrenoSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """
    class Meta:
            model = Terreno
            geo_field = "geom"
            # you can also explicitly declare which fields you want to include
            # as with a ModelSerializer.
            fields = ('npn', 'area_digitada')


class ConstruccionSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """
    class Meta:
            model = Construccion
            geo_field = "geom"
            # you can also explicitly declare which fields you want to include
            # as with a ModelSerializer.
            fields = ('npn', 'identificador','tipo_construccion','area_construida','numero_pisos')

class PredioSerializer(serializers.ModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """
    terrenos = serializers.SerializerMethodField()
    class Meta:
            model = Predio
            # you can also explicitly declare which fields you want to include
            # as with a ModelSerializer.
            fields = '__all__'
    
    def get_terrenos(self,obj):
          instance_terreno = Terreno.objects.filter(npn = obj.npn).first()
          serializer = TerrenoSerializer(instance_terreno)
          return serializer.data
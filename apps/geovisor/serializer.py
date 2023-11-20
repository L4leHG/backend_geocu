from rest_framework_gis.serializers import GeoFeatureModelSerializer
from apps.geovisor.models import Terreno

class TerrenoSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """
    class Meta:
            model = Terreno
            geo_field = "geom"
            # you can also explicitly declare which fields you want to include
            # as with a ModelSerializer.
            fields = ('npn', 'area_digitada')
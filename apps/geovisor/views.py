from .models import Terreno, Predio, Construccion
from rest_framework import generics, response, serializers, response
from .serializer import TerrenoSerializer, ConstruccionSerializer, PredioSerializer
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

# Create your views here.
class TerrenoListApiView(generics.ListAPIView):
    serializer_class = TerrenoSerializer

    def list(self, request, npn):
        instance_terenos = Terreno.objects.filter(npn = npn)
        serializer = self.serializer_class(instance_terenos, many=True)
        return response.Response(serializer.data)
    
# Create your views here.
class ConstruccionListApiView(generics.ListAPIView):
    serializer_class = ConstruccionSerializer

    def list(self, request, npn):
        instance_construccion = Construccion.objects.filter(npn = npn)
        serializer = self.serializer_class(instance_construccion, many=True)
        return response.Response(serializer.data)
    
class PredioListApiView(generics.ListAPIView):
    

    serializer_class = PredioSerializer
    queryset = Predio.objects.all()

    def list(self, request, npn):
        respuesta = {
            'data':'',
            'message':'Consulta exitosa',
            'status':1
        }
        # instance_predio = Predio.objects.filter(npn = npn)
        # if instance_predio.exists() == False:
        #     respuesta['message'] = f'El {npn} no existe'
        #     respuesta['status'] = 0
        #     return response.Response(respuesta)

        try:
            instance_predio = Predio.objects.get(npn = npn)
        except ObjectDoesNotExist:
            respuesta['message'] = f'El {npn} no existe'
            respuesta['status'] = 0
            return response.Response(respuesta)
        except MultipleObjectsReturned:
            respuesta['message'] = f'El {npn} se encuentra repetido'
            respuesta['status'] = 0
            return response.Response(respuesta)
        
        serializer = self.serializer_class(instance_predio)
        respuesta['data'] = serializer.data
        return response.Response(respuesta)


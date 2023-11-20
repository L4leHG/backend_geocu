from .models import Terreno, Predio
from rest_framework import generics, response
from .serializer import TerrenoSerializer

# Create your views here.
class TerrenoListApiView(generics.ListAPIView):
    serializer_class = TerrenoSerializer

    def list(self, request, npn):
        instance_terenos = Terreno.objects.filter(npn = npn)
        serializer = self.serializer_class(instance_terenos, many=True)
        return response.Response(serializer.data)
    


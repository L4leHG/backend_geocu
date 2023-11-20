from django.urls import path, include
from django.views.static import serve

from .views import TerrenoListApiView

urlpatterns = [
    path('geojson/<npn>', TerrenoListApiView.as_view(), name='index'),
]
from django.urls import path, include
from django.views.static import serve

from .views import TerrenoListApiView, PredioListApiView

urlpatterns = [
    path('geojson/<npn>', PredioListApiView.as_view(), name='index'),
]
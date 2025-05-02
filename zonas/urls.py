from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ZonaAgricolaViewSet, convertir_temperatura

router = DefaultRouter()
router.register(r'zonas', ZonaAgricolaViewSet, basename='zonas')

urlpatterns = [
    path('', include(router.urls)),
    path('temperatura/convertir/', convertir_temperatura),
]

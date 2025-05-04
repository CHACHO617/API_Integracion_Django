from rest_framework import serializers # type: ignore
from .models import ZonaAgricola # type: ignore

class ZonaAgricolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZonaAgricola
        fields = ['id', 'nombre', 'cultivo_principal', 'hectareas', 'latitud', 'longitud']

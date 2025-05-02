from django.shortcuts import render  # Si no se usa, puedes eliminarlo

from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from zeep import Client

from .models import ZonaAgricola
from .serializer import ZonaAgricolaSerializer  # type: ignore


class ZonaAgricolaViewSet(viewsets.ModelViewSet):
    queryset = ZonaAgricola.objects.all()
    serializer_class = ZonaAgricolaSerializer


@api_view(['GET'])
def convertir_temperatura(request):
    valor_celsius = request.GET.get('valor')

    if valor_celsius is None:
        return Response(
            {'error': 'El parámetro "valor" es requerido.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        client = Client('https://www.w3schools.com/xml/tempconvert.asmx?WSDL')
        resultado = client.service.CelsiusToFahrenheit(valor_celsius)

        return Response({
            'celsius': float(valor_celsius),
            'fahrenheit': float(resultado),
        })

    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

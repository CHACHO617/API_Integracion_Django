from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="ClimaSeguro API",
        default_version='v1',
        description="API para registrar zonas agrícolas y convertir temperatura",
        contact=openapi.Contact(email="contacto@climaseguro.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from clientes.api import viewsets as clientesviewsets
from servico.api import viewsets as servicoviewsets

# Definindo as rotas para as views
route = routers.DefaultRouter()
route.register(r'clientes', clientesviewsets.ClienteViewSet, basename="clientes")
route.register(r'servico', servicoviewsets.ServicoViewSet, basename="servicos")
route.register(r'carros', clientesviewsets.CarroViewSet, basename="carros")

# Configurando a documentação Swagger
schema_view = get_schema_view(
   openapi.Info(
       title="SwaggerLavaJato",
       default_version='v1',
       description="API",
       terms_of_service="https://www.suaapi.com/terms/"
   ),
   public=False,
   permission_classes=(permissions.AllowAny,),
)

# Configurando as URLs
urlpatterns = [
    path("admin/", admin.site.urls),
    path("clientes/", include('clientes.urls')),
    path("servico/", include('servico.urls')),
    path("admin_black/", include('admin_black.urls')),
    path("", include('home.urls')),
    path("api/", include(route.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

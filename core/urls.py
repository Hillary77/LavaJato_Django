"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from clientes.api import viewsets as clientesviewsets
from servico.api import viewsets as servicoviewsets

route = routers.DefaultRouter()
route.register(r'clientes', clientesviewsets.ClienteViewSet, basename="clientes")
route.register(r'servico', servicoviewsets.ServicoViewSet, basename="servicos")
route.register(r'carros', clientesviewsets.CarroViewSet, 
basename="carros")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("clientes/", include('clientes.urls')),
    path("servico/", include('servico.urls')),
    path("admin_black/", include('admin_black.urls')),
    path("", include('home.urls')),
    path("api/", include(route.urls)),
]

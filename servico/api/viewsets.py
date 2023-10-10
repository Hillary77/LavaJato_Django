from rest_framework import viewsets
from servico.api import serializers
from servico import models

class ServicoViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.ServicoSerializer
  queryset = models.Servico.objects.all()
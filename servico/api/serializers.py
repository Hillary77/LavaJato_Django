from rest_framework import serializers
from servico import models

class ServicoSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Servico
    fields = '__all__' 
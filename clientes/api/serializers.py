from rest_framework import serializers
from clientes.models import Cliente, Carro

#Trata dados do banco e encaminha para viewsets
class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    carros = CarroSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = '__all__'

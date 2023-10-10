from rest_framework import viewsets
from clientes.api import serializers
from clientes.models import Cliente, Carro

#Traz os dados do serializer e joga na parte visual do api rest framework 
class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClienteSerializer
    queryset = Cliente.objects.all()

class CarroViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CarroSerializer
    queryset = Carro.objects.all()

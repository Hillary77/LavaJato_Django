from django import forms
from .models import Cliente, Carro

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente, Carro
        fields = ['user', 'email', 'nome', 'sobrenome', 'endereco', 'cidade', 'cpf', 'cep', 'carro', 'placa', 'ano']
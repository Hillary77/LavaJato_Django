from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['user', 'email', 'nome', 'sobrenome', 'endereco', 'cidade', 'cpf', 'cep']
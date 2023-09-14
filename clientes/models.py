from django.db import models

# Create your models here.
 
class Cliente(models.Model):
    user = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    cpf = models.IntegerField()
    cep = models.IntegerField()
    

    def __str__(self) -> str:
        return self.nome
    

class Carro(models.Model):
    carro = models.CharField(max_length=50)
    placa = models.CharField(max_length=9)
    ano = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    lavagens = models.IntegerField(default=0)
    consertos = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.carro
    


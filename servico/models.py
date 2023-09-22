
from secrets import token_hex, token_urlsafe
from django.db import models
from clientes.models import Cliente
from .choices import ChoicesCategoriaManutencao
from datetime import datetime

class CategoriaManutencao(models.Model):
    titulo = models.CharField(max_length=100, choices=ChoicesCategoriaManutencao.choices)
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self) -> str:
        return self.titulo

# Create your models here.
class Servico(models.Model):
    titulo = models.CharField(max_length=100)  # Corrección aquí
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    categorias_manutencao = models.ManyToManyField(CategoriaManutencao)
    data_init = models.DateField(null=True)
    data_end = models.DateField(null=True)
    finalizado = models.BooleanField(default=False)
    protocolo = models.CharField(max_length=52, null=True, blank=True)
   
    def __str__(self) -> str:
        return self.titulo
    
    def save(self, *args, **kwargs):
        if not self.protocolo:
            #Gerar protocolo de forma aleatoria e salva no banco de dados 
            self.protocolo = datetime.now().strftime("%d/%m/%Y-%H:%M:%S-") + token_hex(16)
       
     
        super(Servico, self).save(*args, **kwargs)

    def valor_total(self):
        valor_total = float(0)
        for categorias in self.categorias_manutencao.all(): 
            valor_total += float(categorias.valor)

        return valor_total
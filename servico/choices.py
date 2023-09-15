# classe das opções das categorias pré definidas para cadastrar
from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
    TROCA_OLEO = 'Troca de óleo',
    TROCA_VALVULA = 'Troca de válvula',
    BALANCEAMENTO =  'Balanceamento',
    LAVAGEM =  'Lavegem',
    LAVA_ASPIRA = 'Lava e aspira' 
      
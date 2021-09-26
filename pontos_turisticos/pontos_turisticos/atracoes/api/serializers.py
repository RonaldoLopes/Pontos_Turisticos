from django.db.models import fields
from pontos_turisticos.atracoes.models import Atracao
from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao

class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('nome', 'descricao', 'horario_func', 'idade_minima')
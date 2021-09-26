from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avalicao

class AvaliacaoSerializer(ModelSerializer):
    class Meta:
        model = Avalicao
        fields = ['id', 'user', 'nota', 'data']
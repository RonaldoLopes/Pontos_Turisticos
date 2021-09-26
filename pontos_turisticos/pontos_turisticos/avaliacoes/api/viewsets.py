from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from avaliacoes.models import Avalicao
from .serializers import AvaliacaoSerializer

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avalicao.objects.all()
    serializer_class = AvaliacaoSerializer
    filter_fields = ('comentario', 'nota')
    filter_backends = (SearchFilter)
    search_fields = ('comentario', 'nota')
from django.db.models import query
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    
    serializer_class = PontoTuristicoSerializer
    #permission_classes = (IsAuthenticated)
    #authentication_classes = (TokenAuthentication)

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass
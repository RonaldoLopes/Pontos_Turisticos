from django.db import models
from django.db.models.deletion import CASCADE
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avalicao
from enderecos.models import Endereco

# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracao = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avalicao)
    endereco = models.ForeignKey(Endereco, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome
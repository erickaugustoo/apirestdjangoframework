from django.db import models
from uuid import uuid4 

# Create your models here.


class Contas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    idConta = models.IntegerField()
    idPessoa = models.IntegerField()
    saldo = models.FloatField()
    limiteSaqueDiario = models.IntegerField()
    flagAtivo = models.BooleanField()
    tipoConta = models.IntegerField()
    dataCriacao = models.DateField(auto_now_add=True)

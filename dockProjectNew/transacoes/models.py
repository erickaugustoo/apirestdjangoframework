from django.db import models
from contas.models import Contas
# Create your models here.

class Transacoes(models.Model):
    idTransacao = models.AutoField(primary_key=True)
    idConta = models.ForeignKey(Contas,on_delete=models.CASCADE)
    valor = models.FloatField()
    dataTransacao = models.DateField(auto_now=True)

    def str(self):
        return self.idTransacao

    class Meta:
        verbose_name_plural = "Transações"
        


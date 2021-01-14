from django.db import models

# Create your models here.

class Pessoas(models.Model):
    idPessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    dataNascimento = models.DateField()

    def str(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Pessoas'

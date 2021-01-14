from rest_framework import viewsets
from transacoes.api import serializers
from transacoes import models

class TransacoesViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.TransacoesSerializer
    queryset = models.Transacoes.objects.all()
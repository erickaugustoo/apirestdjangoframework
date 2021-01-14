from rest_framework import serializers
from transacoes import models

class TransacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Transacoes
        fields = '__all__'
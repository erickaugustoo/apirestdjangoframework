from rest_framework import serializers
from contas import models

class ContasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contas
        fields = '__all__'
        
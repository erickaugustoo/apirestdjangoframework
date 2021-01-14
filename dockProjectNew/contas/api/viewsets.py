from rest_framework import viewsets
from contas.api import serializers
from contas import models

class ContasViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.ContasSerializer
    queryset = models.Contas.objects.all()

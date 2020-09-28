from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from perfil.contas.models import Conta
from perfil.contas.serializers import ContasSerializer

class ContasViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContasSerializer
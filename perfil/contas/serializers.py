from perfil.contas.models import Conta
from rest_framework import serializers

class ContasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        #fields = ['id', 'nome', 'sobrenome', 'genero', 'email', 'data_de_nascimento',
        #          'portador_de_deficiencia', 'cidade', 'estado', 'foto',]
        fields = '__all__'
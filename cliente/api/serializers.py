from dataclasses import fields
from rest_framework import serializers
from cliente.models import Cliente, Banco

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class BancoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banco
        fields = '__all__'

class ClienteDetalhesSerializer(serializers.ModelSerializer):
    banco = BancoSerializers(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = [
        'nome',
        'telefone',
        'endereco',
        'data_de_cadastro',
        'faturamento_declarado',
        'banco',
        ]


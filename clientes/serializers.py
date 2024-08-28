from rest_framework import serializers
from .models import Cliente, Contrato, Endereco, Telefone

class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = '__all__'

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    contratos = ContratoSerializer(many=True, required=False)
    endereco = EnderecoSerializer(required=False)
    telefones = TelefoneSerializer(many=True, required=False)

    class Meta:
        model = Cliente
        fields = ['cpf', 'nb', 'nome', 'data_nasc', 'contratos', 'endereco', 'telefones']

    def create(self, validated_data):
        contratos_data = validated_data.pop('contratos', [])
        endereco_data = validated_data.pop('endereco', {})
        telefones_data = validated_data.pop('telefones', [])

        cliente = Cliente.objects.create(**validated_data)
        
        if endereco_data:
            endereco_data['cliente'] = cliente
            Endereco.objects.create(**endereco_data)

        for contrato_data in contratos_data:
            contrato_data['cliente'] = cliente
            Contrato.objects.create(**contrato_data)
        
        for telefone_data in telefones_data:
            telefone_data['cliente'] = cliente
            Telefone.objects.create(**telefone_data)

        return cliente

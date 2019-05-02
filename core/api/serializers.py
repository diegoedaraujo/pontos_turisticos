from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from core.models import PontoTuristico, Atracao, DocIdentificacao
from atracoes.api.serializers import AtracaoSerializer
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco

class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'

class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = '__all__'
        read_only_fields = ('comentarios')

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracao.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doc1 = DocIdentificacao.objects.create(**doc)

        avaliacoes = validated_data['avaliacoes']
        del validated_data['avaliacoes']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        ponto.avaliacoes.set(avaliacoes)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doc1

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '{0} - {1}'.format(obj.nome, obj.descricao)
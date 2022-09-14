from rest_framework import serializers
from .models import Tarefa, Contato

class RelatedFieldAlternative(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = kwargs.pop('serializer', None)
        if self.serializer is not None and not issubclass(self.serializer, serializers.Serializer):
            raise TypeError('"serializer" is not a valid serializer class')

        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False if self.serializer else True

    def to_representation(self, instance):
        if self.serializer:
            return self.serializer(instance, context=self.context).data
        return super().to_representation(instance)


class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'        

class TarefaSerializer(serializers.ModelSerializer):
    contato = RelatedFieldAlternative(queryset=Contato.objects.all(), serializer=ContatoSerializer)

    class Meta:
        model = Tarefa
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['contato'] = ContatoSerializer(instance.contato).data
        return response    


from rest_framework import serializers
from consumer.models import ConsumerType, Consumer

class CalculatorInputSerializer(serializers.Serializer):
    consumption1 = serializers.FloatField(required=True)
    consumption2 = serializers.FloatField(required=True)
    consumption3 = serializers.FloatField(required=True)
    distributor_tax = serializers.FloatField(required=True)

    tax_type_choices = [(i.value, i.value) for i in ConsumerType]
    tax_type = serializers.ChoiceField(choices=tax_type_choices, required=True)

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = '__all__'
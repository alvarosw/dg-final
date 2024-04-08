from django import forms
from .models import ConsumerType

class CalculatorForm(forms.Form):
    consumption1 = forms.IntegerField(required=True, label='Consumo no Primeiro Mês')
    consumption2 = forms.IntegerField(required=True, label='Consumo no Segundo Mês')
    consumption3 = forms.IntegerField(required=True, label='Consumo no Terceiro Mês')

    distributor_tax = forms.FloatField(required=True, label='Taxa da Distribuidora')

    tax_type_choices = [(i.value, i.value) for i in ConsumerType]
    tax_type = forms.ChoiceField(choices=tax_type_choices, required=True, label='Tipo de Taxa')
